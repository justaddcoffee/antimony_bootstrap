# Strategy: Module Decomposition for Alzheimer's Disease ODE Model

**Date**: 2026-02-24
**Target**: Elbert-scale model (~50 compartments, hundreds of species, ~800 reactions)
**Framework**: antimony_bootstrap ModuleSpec YAML -> Antimony -> SBML -> Tellurium

---

## 1. Module Organization Principles

### 1.1 Decomposition by Biological Pathway

The Alzheimer's disease model should be decomposed into modules that correspond to distinct biological pathways and mechanisms. Each module is a self-contained ModuleSpec YAML file with its own compartments, species, reactions, parameters, and evidence. The guiding principle: **each module should be independently simulatable** (with stub values for external species) and **biologically meaningful** as a unit.

### 1.2 Proposed Module Hierarchy

The model is organized into **4 tiers** reflecting causal ordering in disease progression:

#### Tier 1: Core Pathology (build first)
These are the most constrained by literature data, the most important for disease progression, and the foundation other modules depend on.

| Module | Description | Est. Reactions | Key Compartments |
|--------|-------------|----------------|------------------|
| `abeta_production` | APP processing, BACE1/gamma-secretase cleavage, AB40/AB42 generation | 15-25 | Neuron, BrainISF |
| `abeta_transport` | AB42 transport across ISF, CSF, Plasma, BBB | 20-30 | BrainISF, CSF, Plasma, BBB |
| `abeta_aggregation` | Monomer -> oligomer -> protofibril -> fibril -> plaque cascade | 20-40 | BrainISF, BrainParenchyma |
| `abeta_clearance` | Enzymatic degradation (IDE, NEP), microglial phagocytosis, perivascular drainage | 15-25 | BrainISF, Microglia, Perivascular |
| `tau_phosphorylation` | Tau kinase/phosphatase balance, GSK3B, CDK5, PP2A | 15-25 | Neuron |
| `tau_aggregation` | Hyperphospho-tau -> paired helical filaments -> neurofibrillary tangles | 10-20 | Neuron |

#### Tier 2: Cellular Response Mechanisms
These modulate Tier 1 processes and are reasonably well-characterized in literature.

| Module | Description | Est. Reactions | Key Compartments |
|--------|-------------|----------------|------------------|
| `neuroinflammation_microglia` | Microglial activation states (M1/M2), cytokine production (TNFa, IL1B, IL6) | 30-50 | Microglia, BrainISF |
| `neuroinflammation_astrocyte` | Astrocyte reactivity, GFAP upregulation, complement cascade | 20-30 | Astrocyte, BrainISF |
| `oxidative_stress` | ROS production, antioxidant defense (SOD, GPx), mitochondrial dysfunction | 15-25 | Neuron, Mitochondria |
| `synaptic_dysfunction` | Synaptic loss, LTP/LTD impairment, NMDA/AMPA receptor dynamics | 20-30 | Synapse, Neuron |
| `calcium_homeostasis` | ER calcium release, SERCA pump, mitochondrial calcium, capacitative entry | 15-25 | Neuron, ER, Mitochondria |
| `apoptosis_neuronal_death` | Caspase cascade, Bcl-2 family balance, DNA damage response | 10-20 | Neuron |

#### Tier 3: Modulatory Pathways
These influence disease progression through indirect mechanisms.

| Module | Description | Est. Reactions | Key Compartments |
|--------|-------------|----------------|------------------|
| `lipid_metabolism` | Cholesterol homeostasis, ApoE isoforms, ceramide/sphingolipids | 20-30 | Neuron, Astrocyte, BrainISF |
| `insulin_signaling` | Brain insulin resistance, IRS1, PI3K/Akt, mTOR pathway | 15-25 | Neuron |
| `autophagy_proteostasis` | Autophagosome formation, lysosomal degradation, UPS pathway | 15-25 | Neuron |
| `metal_homeostasis` | Iron, copper, zinc interactions with AB42, ferroptosis | 10-15 | Neuron, BrainISF |
| `bbb_integrity` | Blood-brain barrier transport, tight junctions, RAGE/LRP1 receptors | 15-25 | BBB, Endothelial, Plasma, BrainISF |
| `vascular` | Cerebral blood flow, cerebral amyloid angiopathy, vessel wall AB deposition | 10-20 | Vessel, Perivascular, BrainISF |

#### Tier 4: Genetic and Systemic Factors
These set initial conditions and modulate parameters across other modules.

| Module | Description | Est. Reactions | Key Compartments |
|--------|-------------|----------------|------------------|
| `apoe_genetics` | ApoE2/3/4 isoform effects on AB clearance, lipid transport | 5-15 | BrainISF, Astrocyte |
| `presenilin_mutations` | PSEN1/PSEN2 effects on gamma-secretase, ER stress | 5-10 | Neuron, ER |
| `app_genetics` | APP duplications/mutations, Swedish/London/Iowa mutations | 5-10 | Neuron |
| `trem2_signaling` | TREM2 variant effects on microglial function | 5-10 | Microglia |
| `peripheral_immune` | Peripheral immune cell infiltration, T cells, monocytes | 10-20 | Plasma, BBB, BrainISF |
| `gut_brain_axis` | Microbiome metabolites, vagal signaling (if in scope) | 5-10 | Gut, Plasma, BrainISF |

**Total estimated**: ~350-600 reactions across ~25 modules. To reach ~800 reactions, expect that Tier 1 and Tier 2 modules will be more detailed than estimated above, with additional species isoforms and compartmental transport reactions.

---

## 2. Key Interface Points Between Modules

### 2.1 Shared Compartments

These compartments appear in multiple modules and must be declared consistently in `model.yaml` `shared_compartments`:

| Compartment | Volume (L) | Used By |
|-------------|-----------|---------|
| BrainISF | 0.25 | Nearly all modules (AB, tau, inflammation, etc.) |
| CSF | 0.14 | Transport, biomarker modules |
| Plasma | 3.0 | Transport, peripheral, BBB modules |
| Neuron | 0.001 (est.) | APP processing, tau, synaptic, calcium |
| Microglia | 0.0005 (est.) | Neuroinflammation, AB clearance |
| Astrocyte | 0.001 (est.) | Neuroinflammation, lipid, calcium |
| Synapse | 0.0001 (est.) | Synaptic dysfunction |
| Mitochondria | 0.0001 (est.) | Oxidative stress, calcium, apoptosis |
| ER | 0.0001 (est.) | Calcium, presenilin, proteostasis |
| BBB | 0.0001 (est.) | Transport, vascular |
| Endothelial | 0.0001 (est.) | BBB integrity |
| BrainParenchyma | 1.0 (est.) | Plaque deposition, aggregation |
| Perivascular | 0.01 (est.) | AB drainage, CAA |
| Vessel | 0.1 (est.) | Vascular |

### 2.2 Shared Species (Cross-Module Interface Points)

These species are produced in one module and consumed/modified in another. They are the critical interface points:

| Species | Produced By | Consumed By |
|---------|-------------|-------------|
| `AB42_BrainISF` | abeta_production | abeta_aggregation, abeta_clearance, abeta_transport, neuroinflammation, synaptic_dysfunction |
| `AB42_oligomer_BrainISF` | abeta_aggregation | synaptic_dysfunction, neuroinflammation, tau_phosphorylation |
| `AB42_plaque_BrainParenchyma` | abeta_aggregation | neuroinflammation_microglia, vascular |
| `pTau_Neuron` | tau_phosphorylation | tau_aggregation, apoptosis |
| `NFT_Neuron` | tau_aggregation | apoptosis, neuronal_death |
| `TNFa_BrainISF` | neuroinflammation_microglia | synaptic_dysfunction, apoptosis, tau_phosphorylation |
| `IL1B_BrainISF` | neuroinflammation_microglia | neuroinflammation_astrocyte, synaptic_dysfunction |
| `IL6_BrainISF` | neuroinflammation_microglia/astrocyte | bbb_integrity, peripheral_immune |
| `ROS_Neuron` | oxidative_stress | apoptosis, tau_phosphorylation, lipid_metabolism |
| `ApoE_BrainISF` | lipid_metabolism, apoe_genetics | abeta_clearance, abeta_aggregation |
| `Insulin_BrainISF` | bbb_integrity (from plasma) | insulin_signaling |
| `Ca_Neuron` | calcium_homeostasis | synaptic_dysfunction, apoptosis |
| `Microglia_active_Microglia` | neuroinflammation_microglia | abeta_clearance |
| `BDNF_BrainISF` | synaptic_dysfunction | apoptosis (pro-survival) |
| `Cholesterol_Neuron` | lipid_metabolism | abeta_production (membrane composition) |

### 2.3 Cross-Module Dependency Graph

```
abeta_production
    |
    v
abeta_transport <---> bbb_integrity
    |
    v
abeta_aggregation <--- metal_homeostasis, lipid_metabolism
    |        |
    v        v
abeta_clearance    neuroinflammation_microglia <---> neuroinflammation_astrocyte
    ^                    |        |
    |                    v        v
    +-- apoe_genetics   synaptic_dysfunction   bbb_integrity
                         |
                         v
                    tau_phosphorylation <--- oxidative_stress, insulin_signaling
                         |
                         v
                    tau_aggregation
                         |
                         v
                    apoptosis_neuronal_death <--- calcium_homeostasis
```

---

## 3. Handling Cross-Module Dependencies

### 3.1 The Shared Species Protocol

When a species is produced in module A and consumed in module B:

1. **Module A** declares the species in its `species:` list with `initial_amount`
2. **Module B** references the species in its `reactions:` (reactants/products) but does NOT re-declare it with a different `initial_amount`
3. The `model.yaml` `shared_compartments` ensures volume parameters are consistent
4. The `composer.py` merges all modules, so the species appears once in the final Antimony output

**Convention**: If two modules both need to modify a shared species, both list it in their `species:` section but only the "primary producer" sets `initial_amount`. The secondary module sets `initial_amount: null` or omits it.

### 3.2 Parameter Namespacing

To avoid parameter name collisions across modules, use the convention:
```
k_{reaction_shortname}_{detail}
```

Examples:
- `k_AB42_prod` (abeta_production module)
- `k_AB42_olig_on` (abeta_aggregation module)
- `k_TNFa_prod_M1` (neuroinflammation_microglia module)

Parameters that are truly shared across modules (e.g., temperature, pH) go in `model.yaml` `shared_parameters`.

### 3.3 Incremental Assembly Strategy

1. Build and validate each module independently using stub values for external species
2. Compose modules pairwise (e.g., abeta_production + abeta_transport) and validate
3. Progressively add modules following the tier ordering
4. At each step: `just validate-modules && just assemble && just validate-antimony && just smoke-test`

---

## 4. Build Priority Order

### Phase 1: Amyloid Core (weeks 1-2)
**Goal**: A simulatable AB42 PK model across brain compartments.

1. **`abeta_production`** -- DONE (exists as initial example)
2. **`abeta_transport`** -- Extend ISF/CSF/Plasma transport, add BBB transport via RAGE/LRP1
3. **`abeta_clearance`** -- Enzymatic (IDE, NEP) and cellular clearance pathways
4. **`abeta_aggregation`** -- Monomer-oligomer-fibril-plaque cascade

**Validation milestone**: Simulate AB42 monomer/oligomer/plaque dynamics over 20 years. Compare to CSF AB42 decline observed clinically.

### Phase 2: Tau Pathology (weeks 3-4)
**Goal**: Coupled amyloid-tau model.

5. **`tau_phosphorylation`** -- GSK3B/CDK5/PP2A balance, AB42 oligomer-driven enhancement
6. **`tau_aggregation`** -- NFT formation kinetics

**Validation milestone**: AB42 oligomers drive tau hyperphosphorylation. NFT accumulation follows amyloid with a lag.

### Phase 3: Neuroinflammation (weeks 5-6)
**Goal**: Inflammatory feedback loops that modulate AB clearance and neuronal damage.

7. **`neuroinflammation_microglia`** -- M1/M2 polarization, cytokine production, AB phagocytosis
8. **`neuroinflammation_astrocyte`** -- Reactive astrogliosis, complement, GFAP

**Validation milestone**: Chronic AB exposure shifts microglia from clearing to pro-inflammatory. Cytokine levels match CSF data.

### Phase 4: Neuronal Damage (weeks 7-8)
**Goal**: Downstream consequences -- synaptic loss, neuronal death.

9. **`synaptic_dysfunction`** -- LTP impairment, synapse loss driven by AB oligomers + TNFa
10. **`oxidative_stress`** -- ROS from mitochondrial dysfunction, feeds back to tau
11. **`calcium_homeostasis`** -- ER stress, mitochondrial calcium overload
12. **`apoptosis_neuronal_death`** -- Caspase activation, neuronal loss

**Validation milestone**: Synaptic density decline correlates with cognitive score proxies.

### Phase 5: Modulatory Systems (weeks 9-12)
**Goal**: Complete the model with modulatory pathways.

13. **`lipid_metabolism`** -- Cholesterol, ApoE effects
14. **`insulin_signaling`** -- Brain insulin resistance
15. **`autophagy_proteostasis`** -- Protein quality control
16. **`bbb_integrity`** -- Barrier function
17. **`metal_homeostasis`** -- Iron/copper/zinc
18. **`vascular`** -- Cerebral amyloid angiopathy

### Phase 6: Genetics and Variants (weeks 13-14)
**Goal**: Parameterize genetic risk variants.

19. **`apoe_genetics`** -- ApoE4 risk modulation
20. **`presenilin_mutations`** -- Familial AD
21. **`trem2_signaling`** -- Microglial risk variant
22. **`app_genetics`** -- APP mutations

---

## 5. Literature Constraint Assessment

### Best-constrained modules (most quantitative literature data):
1. **abeta_production/transport/clearance** -- Extensive PK data from clinical trials (solanezumab, aducanumab, lecanemab), CSF biomarker studies, and the Elbert model itself
2. **tau_phosphorylation** -- Kinase rate constants well-characterized in vitro (GSK3B, CDK5)
3. **abeta_aggregation** -- In vitro kinetics extensively studied (ThT fluorescence, AFM)
4. **lipid_metabolism** -- Cholesterol/ApoE transport well-characterized in hepatic models, adaptable

### Moderately constrained:
5. **neuroinflammation** -- Cytokine production rates from in vitro microglial cultures
6. **oxidative_stress** -- ROS production rates from mitochondrial studies
7. **calcium_homeostasis** -- Extensive calcium signaling literature from other contexts

### Least constrained (most assumed parameters):
8. **synaptic_dysfunction** -- Qualitative mechanisms well-known but rate constants sparse
9. **apoptosis** -- Caspase kinetics known but brain-specific rates uncertain
10. **bbb_integrity** -- Transport rates measurable but cellular mechanism rates uncertain
11. **vascular/CAA** -- Mostly qualitative clinical observations
12. **gut_brain_axis** -- Very early-stage research

---

## 6. Validation Strategy for Incremental Build

### Per-Module Validation (at every step)
```bash
just validate-modules   # Schema check: all required fields present
just assemble           # Antimony generation: no syntax errors
just validate-antimony  # antimony.loadString() succeeds
just smoke-test         # tellurium simulate: no NaN, no negative species
```

### Cross-Module Integration Tests
After composing N modules together:
1. **Mass conservation**: Total AB42 across all compartments should be conserved (production - degradation)
2. **Steady state**: Model reaches biologically plausible steady state for healthy baseline
3. **Perturbation response**: Increasing AB production rate should increase AB42 levels downstream
4. **Time scale**: Disease progression should occur over years, not seconds or millennia

### Biological Plausibility Checks
| Metric | Expected Range | Source |
|--------|---------------|--------|
| CSF AB42 concentration | 500-1000 pg/mL (healthy) | Clinical biomarker literature |
| CSF AB42 decline in AD | 40-60% reduction | Blennow et al. |
| CSF p-tau increase | 2-3x elevation in AD | Hansson et al. |
| Plaque deposition onset | 15-20 years before symptoms | Jack et al. biomarker cascade |
| Synaptic loss at MCI | ~20-30% | Terry et al. |

### Comparison to Elbert Reference Model
When available, compare module outputs to corresponding subsystems of the Elbert_Esguerra model:
- Species steady-state concentrations should be within an order of magnitude
- Parameter values should match where sourced from same model
- Dynamic responses to standard perturbations should be qualitatively similar

---

## 7. Technical Considerations

### 7.1 Stiff ODE Systems
The full model will likely be stiff (fast binding reactions + slow disease progression). Ensure tellurium uses an appropriate integrator (CVODE with BDF method, not explicit Euler).

### 7.2 Units Consistency
All modules must use consistent units:
- **Time**: hours (hr)
- **Amount**: moles (mol)
- **Volume**: liters (L)
- **Concentration**: mol/L (M)
- **Rate constants**: appropriate units for reaction order (1/hr, L/mol/hr, etc.)

### 7.3 Naming Collision Prevention
Before adding a new module, run:
```python
# Check for species name collisions
existing_species = set()
for module in existing_modules:
    existing_species.update(module.get_all_species_names())
new_species = set(new_module.get_all_species_names())
collisions = existing_species & new_species
# Collisions are OK only for intentionally shared species
```

### 7.4 Module Size Guidelines
- Target: 10-30 reactions per module
- If a module exceeds 50 reactions, consider splitting into sub-modules
- If a module has fewer than 5 reactions, consider merging with a related module

---

## 8. Summary

The decomposition strategy follows a **pathway-based, tiered approach**:
- **25 modules** organized into 4 tiers reflecting causal ordering
- **Amyloid cascade modules first** (best literature data, foundation for all others)
- **Shared species** are the critical interface between modules, managed by convention
- **Incremental validation** at every step using the 4-level validation pipeline
- **Phase 1 (amyloid core)** can begin immediately, building on the existing `abeta_production` module

The key risk is parameter uncertainty in later-tier modules. Mitigation: use the Elbert reference model as primary parameter source, supplement with literature mining from the 3000-paper corpus in `data/alz_papers_3k/`, and mark uncertain parameters with `confidence: assumed` for later refinement.
