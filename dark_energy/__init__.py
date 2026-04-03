"""Dark energy — observational evidence and the vacuum catastrophe."""

from gaia.lang import claim, contradiction, question, setting

# ── Settings ──
flat_universe = setting(
    "CMB measurements (Planck 2018): universe is spatially flat."
)
flat_universe.label = "flat_universe"

gr_valid = setting(
    "General relativity valid at cosmological scales; Friedmann equations govern expansion."
)
gr_valid.label = "gr_valid"

# ── Observations ──
sn_observation = claim(
    r"Type Ia supernovae (Riess 1998, Perlmutter 1999): "
    r"distant SNe Ia are $\sim 0.2\,\text{mag}$ fainter — expansion is accelerating."
)
sn_observation.label = "sn_observation"

cmb_data = claim(
    r"CMB power spectrum (Planck 2018): $\Omega_\text{total} = 1.000 \pm 0.002$, "
    r"$\Omega_\Lambda \approx 0.68$."
)
cmb_data.label = "cmb_data"

# ── Dark energy fraction ──
dark_energy_fraction = claim(
    r"Dark energy: $\Omega_\Lambda \approx 0.68$ of total energy budget.",
    given=[sn_observation, cmb_data],
)
dark_energy_fraction.label = "dark_energy_fraction"

# ── QFT vacuum energy ──
qft_vacuum_energy = claim(
    r"QFT predicts vacuum energy density $\rho_\text{vac} \sim 10^{76}\,\text{GeV}^4$, "
    r"vastly exceeding observed $\rho_\Lambda$."
)
qft_vacuum_energy.label = "qft_vacuum_energy"

# ── Vacuum catastrophe ──
vacuum_catastrophe = contradiction(
    dark_energy_fraction,
    qft_vacuum_energy,
    reason="Observed dark energy density disagrees with QFT vacuum energy "
           "by ~120 orders of magnitude.",
)
vacuum_catastrophe.label = "vacuum_catastrophe"

# ── Cross-validation ──
cmb_power_spectrum = claim(
    r"Planck CMB power spectrum: independent $\Omega_\Lambda = 0.6847 \pm 0.0073$."
)
cmb_power_spectrum.label = "cmb_power_spectrum"

cross_validation = claim(
    r"Dark energy $\Omega_\Lambda \approx 0.68$ confirmed by independent probes.",
    given=[dark_energy_fraction, cmb_power_spectrum],
)
cross_validation.label = "cross_validation"

# ── Question ──
nature_question = question(
    r"Is dark energy a cosmological constant $\Lambda$ or dynamical quintessence?"
)
nature_question.label = "nature_question"

__all__ = [
    "sn_observation", "cmb_data", "dark_energy_fraction",
    "qft_vacuum_energy", "vacuum_catastrophe",
    "cmb_power_spectrum", "cross_validation",
]
