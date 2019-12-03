"""A json-like master list of workflows and steps."""
# NOTE: Change these values to your workflows and steps in your environment.

WF_STEPS = {
    "dev": {
        "chimerism": (
            "CS-Chimerism Testing (GP24) vDec18", "CS-Sort Chimerism Samples"),
        "gce": (
            "CS-MassArray Genotyping GCE", "CS-Sort DNA Extraction Samples"),
        "pgx": (
            "CS-MassArray Genotyping PGx", "CS-Sort DNA Extraction Samples"),
    },
    "prod": {
        "chimerism": (
            "CS-Chimerism Testing (GP24) vDec18", "CS-Sort Chimerism Samples"),
        "gce": (
            "CS-MassArray Genotyping GCE", "CS-Sort DNA Extraction Samples"),
        "pgx": (
            "CS-MassArray Genotyping PGx", "CS-Sort DNA Extraction Samples"),
    }
}
