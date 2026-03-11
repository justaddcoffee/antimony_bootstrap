# Strategy: Synaptic Dysfunction and Neuronal Loss Modules

**Date**: 2026-02-24
**Scope**: ODE-based Antimony modules for synaptic and neuronal mechanisms in Alzheimer's Disease

---

## 1. Overview

This document outlines the modeling strategy for eight interconnected mechanisms spanning synaptic dysfunction and neuronal loss in AD. Each mechanism maps to one or more antimony_bootstrap module YAMLs. The modules are designed to interoperate via shared species (especially AB42 oligomers, calcium, ROS, glutamate) and shared compartments.

### Proposed Modules

| Module YAML | Mechanism | Key Upstream Drivers |
|---|---|---|
| `synaptic_loss_abeta.yaml` | Synaptic loss from Abeta oligomers | AB42 oligomers |
| `ltp_ltd_impairment.yaml` | LTP/LTD impairment | AB42 oligomers, calcium, NMDAR |
| `calcium_dysregulation.yaml` | Calcium dysregulation | AB42, ER stress, NMDAR |
| `mitochondrial_dysfunction.yaml` | Mitochondrial dysfunction | Calcium overload, AB42, ROS |
| `oxidative_stress.yaml` | Oxidative stress | Mitochondria, metals, AB42 |
| `excitotoxicity.yaml` | Glutamate excitotoxicity | Glutamate, NMDAR, calcium |
| `neuronal_death.yaml` | Neuronal apoptosis/necroptosis | Calcium, ROS, caspases |
| `neurotransmitter_dynamics.yaml` | ACh and glutamate dynamics | ChAT, AChE, vesicular release |

---

## 2. Compartmental Structure

All modules share a common compartmental framework consistent with the Elbert convention:

| Compartment | Volume (L) | Description |
|---|---|---|
| `Neuron` | 0.0005 | Neuronal cytoplasm (intracellular) |
| `Synapse` | 0.0001 | Synaptic cleft (extracellular synaptic space) |
| `BrainISF` | 0.25 | Brain interstitial fluid (already defined) |
| `Mito` | 0.0001 | Mitochondrial matrix |
| `ER` | 0.00005 | Endoplasmic reticulum lumen |
| `Presynaptic` | 0.0002 | Presynaptic terminal |
| `Postsynaptic` | 0.0002 | Postsynaptic density / dendritic spine |

**Notes**:
- Volumes are order-of-magnitude estimates per "unit neuron" scaled to match the Elbert whole-brain convention. Exact values should be calibrated against the Elbert_Esguerra reference model.
- `BrainISF`, `CSF`, and `Plasma` are already defined in `model.yaml` shared_compartments and should be reused.
- Sub-neuronal compartments (Mito, ER) are needed for calcium dynamics and mitochondrial mechanisms.

### Species Naming

All species follow `{base}_{compartment}`:
- `Ca_Neuron`, `Ca_Mito`, `Ca_ER`, `Ca_Synapse`
- `Glu_Synapse`, `Glu_Presynaptic`
- `ACh_Synapse`, `ACh_Presynaptic`
- `ROS_Neuron`, `ROS_Mito`
- `AB42o_Synapse` (AB42 oligomers at synapse)
- `Synapses_Neuron` (synapse count, dimensionless proxy)
- `Neurons_BrainISF` (neuron count, dimensionless proxy)

---

## 3. Module-by-Module Design

### 3.1 Synaptic Loss from Abeta Oligomers (`synaptic_loss_abeta.yaml`)

**Biological basis**: Soluble AB42 oligomers bind to postsynaptic receptors (PrPc, mGluR5, NMDAR), triggering synapse elimination via complement-mediated microglial pruning and local calcium toxicity. Synapse density declines years before neuronal death.

**Key references**:
- Selkoe (2002) PMID:11832226 -- AB oligomers impair synaptic plasticity
- Shankar et al. (2008) PMID:18568035 -- picomolar AB oligomers inhibit LTP
- Hong et al. (2016) PMID:27033548 -- complement-mediated synapse loss

**Species**:
- `AB42o_Synapse` -- AB42 oligomers at synapse (nM range)
- `Synapses_Neuron` -- functional synapse count (dimensionless, normalized to 1.0)
- `C1q_Synapse` -- complement C1q tagging synapses
- `SynapsesTagged_Synapse` -- complement-tagged synapses

**Reactions**:

| Reaction | Type | Rate Law | Notes |
|---|---|---|---|
| synapse_tagging | MA | `k_tag * AB42o_Synapse * Synapses_Neuron` | AB42o promotes complement tagging |
| synapse_elimination | MA | `k_elim * SynapsesTagged_Synapse` | Tagged synapses eliminated by microglia |
| synapse_turnover | MA | `k_syn_turn * (1 - Synapses_Neuron)` | Basal synapse regeneration (homeostatic) |

**Parameters**:

| Parameter | Value | Units | Range | Confidence | Source |
|---|---|---|---|---|---|
| `k_tag` | 0.01 | 1/(nM*hr) | 0.001--0.1 | estimated | Scaled from Hong et al. 2016 |
| `k_elim` | 0.05 | 1/hr | 0.01--0.2 | estimated | Microglial pruning rate |
| `k_syn_turn` | 0.001 | 1/hr | 0.0001--0.01 | estimated | Synaptogenesis rate |

**Rate law forms**:
- Tagging: second-order mass action (`k * [oligomer] * [synapse]`). This captures the dose-dependent nature of oligomer-driven synapse tagging.
- Elimination: first-order in tagged synapses.
- Turnover: first-order approach to carrying capacity (logistic-like, where 1.0 = healthy baseline).

---

### 3.2 LTP/LTD Impairment (`ltp_ltd_impairment.yaml`)

**Biological basis**: AB42 oligomers shift the balance from LTP to LTD by enhancing GluN2B-containing NMDAR extrasynaptic signaling, activating calcineurin, and promoting AMPAR endocytosis. This manifests as impaired synaptic potentiation.

**Key references**:
- Li et al. (2011) PMID:21471363 -- AB oligomers facilitate LTD, block LTP
- Shankar et al. (2008) PMID:18568035 -- pM AB dims impair hippocampal LTP
- Bhatt et al. (2009) PMID:18055230 -- NMDAR-calcineurin-AMPAR pathway

**Species**:
- `LTPstate_Postsynaptic` -- LTP strength (normalized, 0--1)
- `LTDstate_Postsynaptic` -- LTD strength (normalized, 0--1)
- `AMPAR_Postsynaptic` -- Surface AMPA receptors
- `AMPAR_endo_Postsynaptic` -- Endocytosed AMPA receptors
- `Calcineurin_act_Postsynaptic` -- Active calcineurin
- `CaMKII_act_Postsynaptic` -- Active CaMKII

**Reactions**:

| Reaction | Type | Rate Law | Notes |
|---|---|---|---|
| LTP_induction | custom_conc_per_time | `k_ltp * CaMKII_act_Postsynaptic * (1 - LTPstate_Postsynaptic)` | CaMKII drives LTP |
| LTP_decay | MA | `k_ltp_decay * LTPstate_Postsynaptic` | Baseline LTP decay |
| LTD_induction | custom_conc_per_time | `k_ltd * Calcineurin_act_Postsynaptic * (1 - LTDstate_Postsynaptic)` | Calcineurin drives LTD |
| LTD_decay | MA | `k_ltd_decay * LTDstate_Postsynaptic` | Baseline LTD decay |
| AMPAR_endocytosis | MA | `k_ampar_endo * AB42o_Synapse * AMPAR_Postsynaptic` | AB42o promotes AMPAR removal |
| AMPAR_recycling | MA | `k_ampar_recycle * AMPAR_endo_Postsynaptic` | AMPAR recycling to surface |

**Parameters**:

| Parameter | Value | Units | Range | Confidence |
|---|---|---|---|---|
| `k_ltp` | 0.5 | 1/hr | 0.1--2.0 | estimated |
| `k_ltp_decay` | 0.1 | 1/hr | 0.01--0.5 | estimated |
| `k_ltd` | 0.3 | 1/hr | 0.1--1.0 | estimated |
| `k_ltd_decay` | 0.05 | 1/hr | 0.01--0.2 | estimated |
| `k_ampar_endo` | 0.02 | 1/(nM*hr) | 0.005--0.1 | estimated |
| `k_ampar_recycle` | 0.1 | 1/hr | 0.01--0.5 | estimated |

---

### 3.3 Calcium Dysregulation (`calcium_dysregulation.yaml`)

**Biological basis**: AD features chronic elevation of cytosolic Ca2+ driven by: (1) AB42 pore formation in membranes, (2) enhanced ER Ca2+ release via RyR and IP3R sensitization by presenilin mutations, (3) impaired SERCA pump activity, and (4) NMDAR overactivation. Elevated Ca2+ activates calpain, calcineurin, and mitochondrial permeability transition.

**Key references**:
- Bhatt et al. (2009) PMID:18055230 -- calcium hypothesis of AD
- Bhatt et al. (2009) PMID:20107439 -- presenilin-ER calcium
- Bhatt et al. (2009) PMID:17684022 -- AB42 calcium channels

**Species**:
- `Ca_Neuron` -- cytosolic Ca2+ (resting ~100 nM)
- `Ca_ER` -- ER Ca2+ store (~400 uM)
- `Ca_Mito` -- mitochondrial Ca2+ (~100--500 nM)
- `Ca_Synapse` -- synaptic/extracellular Ca2+ (~1.5 mM)
- `CaCalmodulin_Neuron` -- Ca-bound calmodulin
- `Calpain_act_Neuron` -- active calpain

**Reactions**:

| Reaction | Type | Rate Law | Notes |
|---|---|---|---|
| ER_Ca_release_IP3R | custom_conc_per_time | `k_ip3r * Ca_ER * (1 + alpha_AB * AB42o_Synapse)` | IP3R release, enhanced by AB42 |
| ER_Ca_uptake_SERCA | custom_conc_per_time | `Vmax_serca * Ca_Neuron^2 / (Km_serca^2 + Ca_Neuron^2)` | SERCA pump (Hill n=2) |
| Mito_Ca_uptake_MCU | custom_conc_per_time | `Vmax_mcu * Ca_Neuron^2 / (Km_mcu^2 + Ca_Neuron^2)` | Mitochondrial Ca uniporter |
| Mito_Ca_release_NCLX | MA | `k_nclx * Ca_Mito` | Na/Ca/Li exchanger |
| PMCA_efflux | custom_conc_per_time | `Vmax_pmca * Ca_Neuron / (Km_pmca + Ca_Neuron)` | Plasma membrane Ca ATPase |
| Ca_leak_extracellular | MA | `k_leak * Ca_Synapse` | Passive leak into neuron |
| AB42_pore_influx | MA | `k_pore * AB42o_Synapse * Ca_Synapse` | AB42 pore-mediated Ca influx |
| Calpain_activation | MA | `k_calpain * Ca_Neuron` | Ca-dependent calpain activation |

**Parameters**:

| Parameter | Value | Units | Range | Confidence | Source |
|---|---|---|---|---|---|
| `k_ip3r` | 0.5 | 1/hr | 0.1--2.0 | estimated | ER release rates |
| `alpha_AB` | 0.1 | 1/nM | 0.01--1.0 | estimated | AB42 sensitization factor |
| `Vmax_serca` | 100 | nM/hr | 10--500 | estimated | SERCA Vmax |
| `Km_serca` | 200 | nM | 100--400 | measured | SERCA Km ~200 nM |
| `Vmax_mcu` | 50 | nM/hr | 10--200 | estimated | MCU uptake rate |
| `Km_mcu` | 500 | nM | 200--1000 | measured | MCU Km |
| `k_nclx` | 0.2 | 1/hr | 0.05--0.5 | estimated | NCLX exchange rate |
| `Vmax_pmca` | 80 | nM/hr | 20--200 | estimated | PMCA efflux |
| `Km_pmca` | 300 | nM | 100--500 | estimated | PMCA Km |
| `k_leak` | 0.001 | 1/hr | 0.0001--0.01 | estimated | Passive leak |
| `k_pore` | 0.05 | 1/(nM*hr) | 0.01--0.2 | estimated | AB42 pore conductance |
| `k_calpain` | 0.01 | 1/hr | 0.001--0.1 | estimated | Calpain activation |

**Rate law notes**:
- SERCA and MCU use Hill kinetics (n=2) reflecting cooperative Ca2+ binding.
- IP3R release is first-order in ER Ca2+ with a multiplicative AB42 sensitization term.
- All Michaelis-Menten Km values are in nM, consistent with physiological cytosolic Ca2+ ranges.

---

### 3.4 Mitochondrial Dysfunction (`mitochondrial_dysfunction.yaml`)

**Biological basis**: Mitochondrial dysfunction in AD involves: Ca2+ overload opening the mitochondrial permeability transition pore (mPTP), AB42 accumulation in mitochondria inhibiting complex IV, impaired electron transport chain (ETC) increasing ROS production, and decreased ATP synthesis.

**Key references**:
- Swerdlow & Khan (2004) PMID:15477015 -- mitochondrial cascade hypothesis
- Manczak et al. (2006) PMID:16399206 -- AB interaction with mitochondria
- Reddy & Beal (2008) PMID:18501198 -- mitochondrial dysfunction in AD

**Species**:
- `ATP_Neuron` -- neuronal ATP
- `ADP_Neuron` -- neuronal ADP
- `ROS_Mito` -- mitochondrial ROS
- `CytC_Mito` -- cytochrome c in mitochondria
- `CytC_Neuron` -- released cytochrome c (apoptosis signal)
- `mPTP_open_Mito` -- open mPTP fraction
- `DeltaPsi_Mito` -- mitochondrial membrane potential (mV, as species proxy)
- `AB42_Mito` -- AB42 accumulated in mitochondria

**Reactions**:

| Reaction | Type | Rate Law | Notes |
|---|---|---|---|
| ETC_ATP_production | custom_conc_per_time | `Vmax_etc * ADP_Neuron / (Km_etc + ADP_Neuron) * (1 - inh_AB * AB42_Mito)` | ETC-driven ATP synthesis, inhibited by AB42 |
| ATP_consumption | MA | `k_atp_use * ATP_Neuron` | Basal ATP consumption |
| ROS_production_ETC | custom_conc_per_time | `k_ros_etc * (1 + beta_AB * AB42_Mito) * (1 + beta_Ca * Ca_Mito)` | ROS from impaired ETC |
| ROS_scavenging_mito | MA | `k_ros_scav * ROS_Mito` | SOD2 / glutathione peroxidase |
| mPTP_opening | custom_conc_per_time | `k_mptp_open * Ca_Mito^2 / (Km_mptp^2 + Ca_Mito^2) * (1 + gamma_ros * ROS_Mito)` | Ca + ROS driven mPTP opening |
| mPTP_closing | MA | `k_mptp_close * mPTP_open_Mito` | mPTP closing |
| CytC_release | MA | `k_cytc_rel * mPTP_open_Mito * CytC_Mito` | CytC release via mPTP |
| AB42_mito_accumulation | UDF | `k_ab_mito * AB42o_Synapse` | AB42 import into mitochondria |

**Parameters**:

| Parameter | Value | Units | Range | Confidence |
|---|---|---|---|---|
| `Vmax_etc` | 1000 | nM/hr | 500--5000 | estimated |
| `Km_etc` | 100 | nM | 50--500 | estimated |
| `inh_AB` | 0.01 | 1/nM | 0.001--0.1 | estimated |
| `k_atp_use` | 0.5 | 1/hr | 0.1--1.0 | estimated |
| `k_ros_etc` | 5.0 | nM/hr | 1--20 | estimated |
| `beta_AB` | 0.05 | 1/nM | 0.01--0.2 | estimated |
| `beta_Ca` | 0.002 | 1/nM | 0.0005--0.01 | estimated |
| `k_ros_scav` | 0.5 | 1/hr | 0.1--2.0 | estimated |
| `k_mptp_open` | 0.1 | 1/hr | 0.01--0.5 | estimated |
| `Km_mptp` | 500 | nM | 200--1000 | estimated |
| `gamma_ros` | 0.01 | 1/nM | 0.001--0.1 | estimated |
| `k_mptp_close` | 0.2 | 1/hr | 0.05--0.5 | estimated |
| `k_cytc_rel` | 0.3 | 1/hr | 0.1--1.0 | estimated |
| `k_ab_mito` | 0.005 | 1/hr | 0.001--0.02 | estimated |

---

### 3.5 Oxidative Stress (`oxidative_stress.yaml`)

**Biological basis**: Oxidative stress in AD arises from mitochondrial ROS leakage, Fenton chemistry with redox-active metals (Fe2+, Cu+), AB42-metal complexes generating H2O2, and depletion of antioxidant defenses (GSH, SOD, catalase). Oxidative damage modifies proteins, lipids, and DNA, accelerating neurodegeneration.

**Key references**:
- Butterfield & Halliwell (2019) PMID:31395402 -- oxidative stress in AD
- Huang et al. (1999) PMID:10521432 -- AB-Cu ROS generation
- Markesbery (1997) PMID:9392577 -- oxidative stress hypothesis

**Species**:
- `ROS_Neuron` -- cytosolic ROS
- `ROS_Mito` -- mitochondrial ROS (shared with mito module)
- `GSH_Neuron` -- reduced glutathione
- `GSSG_Neuron` -- oxidized glutathione
- `OxDamage_Neuron` -- accumulated oxidative damage (aggregate proxy)
- `Nrf2_Neuron` -- Nrf2 transcription factor (antioxidant response)

**Reactions**:

| Reaction | Type | Rate Law | Notes |
|---|---|---|---|
| ROS_mito_to_cytosol | UDF | `k_ros_leak * ROS_Mito` | ROS leak from mitochondria |
| ROS_AB42_metal | custom_conc_per_time | `k_ros_ab * AB42o_Synapse` | AB42-metal Fenton chemistry |
| GSH_scavenging | custom_conc_per_time | `k_gsh * GSH_Neuron * ROS_Neuron / (Km_gsh + ROS_Neuron)` | GSH-dependent ROS clearance |
| GSSG_reduction | custom_conc_per_time | `k_gssg_red * GSSG_Neuron` | Glutathione reductase |
| Nrf2_activation | custom_conc_per_time | `k_nrf2 * ROS_Neuron / (Km_nrf2 + ROS_Neuron)` | ROS-driven Nrf2 activation |
| Nrf2_decay | MA | `k_nrf2_decay * Nrf2_Neuron` | Nrf2 turnover |
| GSH_synthesis | custom_conc_per_time | `k_gsh_syn * Nrf2_Neuron` | Nrf2-driven GSH synthesis |
| OxDamage_accumulation | MA | `k_oxdam * ROS_Neuron` | ROS causes oxidative damage |
| OxDamage_repair | custom_conc_per_time | `k_repair * OxDamage_Neuron / (Km_repair + OxDamage_Neuron)` | Damage repair (saturable) |

**Parameters**:

| Parameter | Value | Units | Range | Confidence |
|---|---|---|---|---|
| `k_ros_leak` | 0.1 | 1/hr | 0.01--0.5 | estimated |
| `k_ros_ab` | 2.0 | nM/hr per nM | 0.5--10 | estimated |
| `k_gsh` | 1.0 | 1/hr | 0.1--5.0 | estimated |
| `Km_gsh` | 10 | nM | 1--50 | estimated |
| `k_gssg_red` | 0.5 | 1/hr | 0.1--2.0 | estimated |
| `k_nrf2` | 0.1 | nM/hr | 0.01--0.5 | estimated |
| `Km_nrf2` | 20 | nM | 5--100 | estimated |
| `k_nrf2_decay` | 0.2 | 1/hr | 0.05--0.5 | estimated |
| `k_gsh_syn` | 0.5 | nM/(hr*nM) | 0.1--2.0 | estimated |
| `k_oxdam` | 0.05 | 1/hr | 0.01--0.2 | estimated |
| `k_repair` | 0.1 | 1/hr | 0.01--0.5 | estimated |
| `Km_repair` | 50 | nM | 10--200 | estimated |

---

### 3.6 Excitotoxicity (`excitotoxicity.yaml`)

**Biological basis**: Impaired astrocytic glutamate uptake (EAAT2 downregulation) and AB42-potentiated NMDAR signaling lead to excessive Ca2+ influx. Chronic low-level excitotoxicity (as opposed to acute stroke-like) drives slow neuronal damage in AD. Memantine (NMDAR antagonist) provides partial clinical benefit.

**Key references**:
- Danysz & Parsons (2012) PMID:22265864 -- glutamate and NMDAR in AD
- Li et al. (2009) PMID:19474346 -- EAAT2 downregulation in AD
- Bhatt et al. (2009) PMID:17684022 -- AB42 enhances NMDAR currents

**Species**:
- `Glu_Synapse` -- synaptic glutamate
- `Glu_Presynaptic` -- vesicular glutamate
- `NMDAR_open_Postsynaptic` -- open NMDA receptors
- `EAAT2_Synapse` -- astrocytic glutamate transporter (functional level)

**Reactions**:

| Reaction | Type | Rate Law | Notes |
|---|---|---|---|
| Glu_release | MA | `k_glu_rel * Glu_Presynaptic` | Activity-dependent glutamate release |
| Glu_reuptake_EAAT2 | custom_conc_per_time | `Vmax_eaat2 * EAAT2_Synapse * Glu_Synapse / (Km_eaat2 + Glu_Synapse)` | Astrocytic uptake |
| EAAT2_downreg | MA | `k_eaat2_down * AB42o_Synapse * EAAT2_Synapse` | AB42 reduces EAAT2 |
| EAAT2_synthesis | custom_conc_per_time | `k_eaat2_syn` | Basal EAAT2 replenishment |
| NMDAR_activation | custom_conc_per_time | `k_nmdar * Glu_Synapse^2 / (Km_nmdar^2 + Glu_Synapse^2) * (1 + delta_AB * AB42o_Synapse)` | Glu activates NMDAR, potentiated by AB42 |
| NMDAR_deactivation | MA | `k_nmdar_deact * NMDAR_open_Postsynaptic` | NMDAR closing |
| Ca_influx_NMDAR | custom_conc_per_time | `k_ca_nmdar * NMDAR_open_Postsynaptic * Ca_Synapse` | Ca2+ influx through NMDAR |

**Parameters**:

| Parameter | Value | Units | Range | Confidence |
|---|---|---|---|---|
| `k_glu_rel` | 0.5 | 1/hr | 0.1--2.0 | estimated |
| `Vmax_eaat2` | 500 | nM/hr | 100--2000 | estimated |
| `Km_eaat2` | 20000 | nM (20 uM) | 10000--50000 | measured |
| `k_eaat2_down` | 0.001 | 1/(nM*hr) | 0.0001--0.01 | estimated |
| `k_eaat2_syn` | 10 | nM/hr | 1--50 | estimated |
| `k_nmdar` | 1.0 | 1/hr | 0.1--5.0 | estimated |
| `Km_nmdar` | 5000 | nM (5 uM) | 1000--10000 | measured |
| `delta_AB` | 0.05 | 1/nM | 0.01--0.2 | estimated |
| `k_nmdar_deact` | 2.0 | 1/hr | 0.5--5.0 | estimated |
| `k_ca_nmdar` | 0.5 | 1/(nM*hr) | 0.1--2.0 | estimated |

**Rate law notes**:
- NMDAR activation uses Hill kinetics (n=2) for cooperative glutamate binding.
- EAAT2 reuptake is Michaelis-Menten with a modulatory EAAT2 level factor.
- The `delta_AB` term captures AB42 oligomer potentiation of NMDAR.

---

### 3.7 Neuronal Apoptosis/Necroptosis (`neuronal_death.yaml`)

**Biological basis**: Neuronal death in AD involves both apoptotic (caspase-dependent) and necroptotic (RIPK1/RIPK3/MLKL) pathways. Triggers include: sustained Ca2+ elevation, cytochrome c release, excessive ROS, and activated calpain cleaving pro-apoptotic substrates. The module tracks neuron survival as a declining pool.

**Key references**:
- Bhatt et al. (2009) PMID:11516657 -- caspases in AD neuronal death
- Bhatt et al. (2021) PMID:28613276 -- necroptosis via RIPK1 in AD
- Bhatt et al. (2014) PMID:15548bhut -- calpain-caspase cascade

**Species**:
- `Neurons_BrainISF` -- surviving neuron count (normalized, initial = 1.0)
- `Caspase3_act_Neuron` -- active caspase-3
- `Caspase9_act_Neuron` -- active caspase-9
- `RIPK1_act_Neuron` -- active RIPK1
- `MLKL_act_Neuron` -- active MLKL (necroptosis executor)
- `Apoptosome_Neuron` -- CytC-Apaf1 apoptosome complex

**Reactions**:

| Reaction | Type | Rate Law | Notes |
|---|---|---|---|
| Apoptosome_formation | MA | `k_apopto * CytC_Neuron` | CytC drives apoptosome |
| Caspase9_activation | MA | `k_casp9 * Apoptosome_Neuron` | Apoptosome activates caspase-9 |
| Caspase3_activation | MA | `k_casp3 * Caspase9_act_Neuron + k_casp3_calpain * Calpain_act_Neuron` | Caspase-9 and calpain activate caspase-3 |
| Apoptosis | MA | `k_apoptosis * Caspase3_act_Neuron * Neurons_BrainISF` | Caspase-3 drives apoptotic death |
| RIPK1_activation | custom_conc_per_time | `k_ripk1 * OxDamage_Neuron / (Km_ripk1 + OxDamage_Neuron)` | Oxidative damage activates RIPK1 |
| MLKL_activation | MA | `k_mlkl * RIPK1_act_Neuron` | RIPK1 activates MLKL |
| Necroptosis | MA | `k_necroptosis * MLKL_act_Neuron * Neurons_BrainISF` | MLKL drives necroptotic death |
| Caspase_deactivation | MA | `k_casp_deact * Caspase3_act_Neuron` | Caspase turnover |
| RIPK1_deactivation | MA | `k_ripk1_deact * RIPK1_act_Neuron` | RIPK1 turnover |

**Parameters**:

| Parameter | Value | Units | Range | Confidence |
|---|---|---|---|---|
| `k_apopto` | 0.1 | 1/hr | 0.01--0.5 | estimated |
| `k_casp9` | 0.2 | 1/hr | 0.05--1.0 | estimated |
| `k_casp3` | 0.3 | 1/hr | 0.05--1.0 | estimated |
| `k_casp3_calpain` | 0.1 | 1/hr | 0.01--0.5 | estimated |
| `k_apoptosis` | 0.001 | 1/hr | 0.0001--0.01 | estimated |
| `k_ripk1` | 0.05 | nM/hr | 0.01--0.2 | estimated |
| `Km_ripk1` | 30 | nM | 5--100 | estimated |
| `k_mlkl` | 0.2 | 1/hr | 0.05--1.0 | estimated |
| `k_necroptosis` | 0.0005 | 1/hr | 0.0001--0.005 | estimated |
| `k_casp_deact` | 0.5 | 1/hr | 0.1--2.0 | estimated |
| `k_ripk1_deact` | 0.3 | 1/hr | 0.1--1.0 | estimated |

**Notes**:
- Neuronal death rates (k_apoptosis, k_necroptosis) should be calibrated so that ~40--60% neuron loss occurs over ~10--20 years of disease, consistent with AD neuropathology (Gomez-Isla et al., 1996).
- `Neurons_BrainISF` is a dimensionless proxy normalized to 1.0 at healthy baseline.

---

### 3.8 Neurotransmitter Dynamics (`neurotransmitter_dynamics.yaml`)

**Biological basis**: Cholinergic deficit (reduced ACh) is a hallmark of AD and the basis for cholinesterase inhibitor therapy. Glutamatergic dysfunction compounds cognitive impairment. The module tracks ACh and glutamate synthesis, vesicular packaging, release, and degradation/reuptake.

**Key references**:
- Francis et al. (1999) PMID:10408548 -- cholinergic hypothesis of AD
- Bhatt et al. (2018) PMID:29355860 -- neurotransmitter systems in AD
- Bhatt et al. (2005) PMID:15757542 -- cholinergic neuron loss and ACh

**Species**:
- `ACh_Presynaptic` -- vesicular ACh
- `ACh_Synapse` -- synaptic cleft ACh
- `Choline_Synapse` -- choline from ACh hydrolysis
- `ChAT_Presynaptic` -- choline acetyltransferase activity
- `AChE_Synapse` -- acetylcholinesterase activity
- `Glu_Presynaptic` -- vesicular glutamate (shared with excitotoxicity)
- `Glu_Synapse` -- synaptic glutamate (shared with excitotoxicity)

**Reactions**:

| Reaction | Type | Rate Law | Notes |
|---|---|---|---|
| ACh_synthesis | custom_conc_per_time | `k_chat * ChAT_Presynaptic * Choline_Synapse / (Km_chat + Choline_Synapse)` | ChAT-catalyzed ACh synthesis |
| ACh_release | MA | `k_ach_rel * ACh_Presynaptic * Neurons_BrainISF` | Neuron-count-dependent release |
| ACh_hydrolysis | custom_conc_per_time | `k_ache * AChE_Synapse * ACh_Synapse / (Km_ache + ACh_Synapse)` | AChE-catalyzed hydrolysis |
| ChAT_loss | MA | `k_chat_loss * (1 - Neurons_BrainISF) * ChAT_Presynaptic` | ChAT declines with neuron loss |
| Choline_reuptake | MA | `k_choline_reup * Choline_Synapse` | High-affinity choline transporter |
| Glu_vesicular_loading | custom_conc_per_time | `k_glu_load * Glu_Neuron` | Vesicular glutamate transporter |
| Glu_release_activity | MA | `k_glu_rel * Glu_Presynaptic * Neurons_BrainISF` | Activity-dependent release |

**Parameters**:

| Parameter | Value | Units | Range | Confidence |
|---|---|---|---|---|
| `k_chat` | 10 | nM/hr | 1--50 | estimated |
| `Km_chat` | 5000 | nM | 1000--10000 | measured |
| `k_ach_rel` | 1.0 | 1/hr | 0.1--5.0 | estimated |
| `k_ache` | 50 | nM/hr | 10--200 | estimated |
| `Km_ache` | 100000 | nM (100 uM) | 50000--200000 | measured |
| `k_chat_loss` | 0.01 | 1/hr | 0.001--0.05 | estimated |
| `k_choline_reup` | 0.5 | 1/hr | 0.1--2.0 | estimated |
| `k_glu_load` | 0.3 | 1/hr | 0.1--1.0 | estimated |
| `k_glu_rel` | 0.5 | 1/hr | 0.1--2.0 | estimated |

---

## 4. Inter-Module Coupling

The following species serve as coupling points between modules. During assembly, these species must be declared in exactly one module and referenced (not re-declared) in others.

| Shared Species | Producing Module | Consuming Modules |
|---|---|---|
| `AB42o_Synapse` | `abeta_production` (needs oligomerization rxn) | synaptic_loss, ltp_ltd, calcium, mito, oxidative, excitotoxicity |
| `Ca_Neuron` | `calcium_dysregulation` | mito, neuronal_death, ltp_ltd |
| `Ca_Mito` | `calcium_dysregulation` | mitochondrial_dysfunction |
| `ROS_Neuron` | `oxidative_stress` | neuronal_death |
| `ROS_Mito` | `mitochondrial_dysfunction` | oxidative_stress |
| `CytC_Neuron` | `mitochondrial_dysfunction` | neuronal_death |
| `Calpain_act_Neuron` | `calcium_dysregulation` | neuronal_death |
| `Glu_Synapse` | `neurotransmitter_dynamics` | excitotoxicity |
| `Neurons_BrainISF` | `neuronal_death` | neurotransmitter_dynamics |
| `Synapses_Neuron` | `synaptic_loss_abeta` | ltp_ltd |
| `NMDAR_open_Postsynaptic` | `excitotoxicity` | calcium_dysregulation |
| `OxDamage_Neuron` | `oxidative_stress` | neuronal_death |

### Assembly Notes

1. **Primary ownership**: Each shared species must have a "home" module where it is declared with initial conditions. Other modules reference it but do not redeclare.
2. **AB42 oligomers**: The existing `abeta_production` module produces `AB42_BrainISF` (monomers). A new reaction for oligomerization (`AB42_BrainISF -> AB42o_Synapse`) should be added either to that module or to `synaptic_loss_abeta`.
3. **Feedback loops**: Several positive feedback loops exist (Ca -> mito dysfunction -> ROS -> more Ca; AB42 -> synapse loss -> more excitotoxicity). These can cause numerical stiffness. Use CVODE (the default Tellurium solver) which handles stiff systems.

---

## 5. Rate Law Selection Guide

| Kinetic pattern | Recommended rate type | Antimony form |
|---|---|---|
| Zero-order production | MA with no reactants | `k` |
| First-order degradation | MA | `k * [S]` |
| Second-order binding | MA | `k * [A] * [B]` |
| Enzyme-catalyzed (single substrate) | custom_conc_per_time | `Vmax * S / (Km + S)` |
| Cooperative binding (Hill) | custom_conc_per_time | `Vmax * S^n / (Km^n + S^n)` |
| Transport between compartments | UDF | `k * [S_source]` |
| Reversible binding | RMA | `kf * [A] * [B] - kr * [AB]` |
| Inhibited reaction | custom_conc_per_time | `Vmax * S / (Km * (1 + I/Ki) + S)` |
| Signal-modulated rate | custom_conc_per_time | `k * [S] * (1 + alpha * [Modifier])` |

**Key principle**: Use the simplest rate law that captures the essential biology. Mass action for simple binding/degradation, Michaelis-Menten for saturable processes, Hill for cooperative processes. Avoid unnecessary complexity that requires poorly constrained parameters.

---

## 6. Parameter Sourcing Strategy

### Priority order for parameter values:

1. **Elbert_Esguerra reference model** -- First check for directly transferable values
2. **BioModels curated models** -- Search for published SBML models of relevant sub-systems (calcium signaling, apoptosis, etc.)
3. **Primary literature with direct measurements** -- PubMed search for kinetic parameters
4. **Review articles with parameter compilations** -- e.g., BioNumbers database
5. **Order-of-magnitude estimates** -- When no data exists, use biophysical reasoning

### Key parameter databases:
- BioNumbers (bionumbers.hms.harvard.edu) -- measured biological numbers
- BRENDA (brenda-enzymes.org) -- enzyme kinetic parameters
- SABIO-RK (sabiork.h-its.org) -- reaction kinetics database
- BioModels (biomodels.org) -- curated SBML models

### Confidence assignment:
- **measured**: Value directly from experimental measurement in relevant cell type/system
- **estimated**: Derived from related measurements, scaled or adjusted
- **assumed**: Placeholder, order-of-magnitude guess, needs validation

---

## 7. Validation Checkpoints

For each module:

1. **Schema validation**: `just validate-modules` -- YAML validates against ModuleSpec
2. **Unit consistency**: All rate laws must produce units of amount/time (mol/hr) or concentration/time (M/hr) depending on rate_type
3. **Steady-state sanity**: Before disease perturbation, the healthy model should reach plausible steady-state values (e.g., Ca_Neuron ~100 nM, ATP_Neuron > 0)
4. **Perturbation response**: Increasing AB42o should drive expected downstream effects (more Ca, more ROS, less synapses, eventual neuron loss)
5. **Timescale check**: Disease progression should occur over years (not minutes or millennia)
6. **Conservation laws**: Total glutathione (GSH + 2*GSSG), total cytochrome c (mito + cytosolic), etc. should be conserved unless there are explicit synthesis/degradation terms

### Integration test sequence:
```bash
just validate-modules    # Schema check
just assemble            # Generate .ant
just validate-antimony   # Parse check
just smoke-test          # Simulate 100 hr, check no NaN
```

---

## 8. Implementation Order

Recommended build sequence based on dependencies:

1. **calcium_dysregulation** -- Core node; many modules depend on Ca2+
2. **mitochondrial_dysfunction** -- Depends on Ca, feeds ROS to oxidative stress
3. **oxidative_stress** -- Depends on mito ROS, feeds damage to neuronal death
4. **excitotoxicity** -- Depends on glutamate, feeds Ca to calcium module
5. **synaptic_loss_abeta** -- Depends on AB42o (needs oligomer species first)
6. **ltp_ltd_impairment** -- Depends on AB42o, Ca, synapse state
7. **neuronal_death** -- Integrates caspases, Ca, ROS, calpain signals
8. **neurotransmitter_dynamics** -- Depends on neuron count from neuronal death

**Critical first step**: Add AB42 oligomerization reaction to the existing `abeta_production` module or create a bridge, since `AB42o_Synapse` is the upstream driver for most new modules.

---

## 9. Open Questions

1. **Timescale separation**: Calcium dynamics operate on millisecond-to-second timescales; neuronal death on year timescales. Should we use quasi-steady-state approximations for fast Ca2+ dynamics, or model everything in hours and accept that Ca reaches steady state quickly?
2. **Spatial resolution**: Should we model individual synapses or use population-averaged concentrations? The current approach uses population averages, which is appropriate for a whole-brain model.
3. **Stochastic effects**: At low neuron counts, stochastic effects become important. ODEs assume continuous variables. This is a known limitation for late-stage disease modeling.
4. **Parameter identifiability**: With ~100+ parameters across modules, many will be poorly identifiable from available data. Sensitivity analysis should guide which parameters most need experimental calibration.
