RED = "\033[93m{"
GREEN = "\033[92m"
BOLD = "\033[1m"
END = "\033[0m"


def bold_red(text: str) -> str:
    return BOLD + RED + text + END + END


def bold_green(text: str) -> str:
    return BOLD + GREEN + text + END + END


def bold(text: str) -> str:
    return BOLD + text + END
