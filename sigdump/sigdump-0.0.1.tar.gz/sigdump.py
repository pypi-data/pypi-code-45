import gc
import os
import signal
import sys
import traceback
from datetime import datetime

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional
    from typing import TextIO
    from types import FrameType

sigdump_signal: 'Optional[str]' = os.getenv("SIGDUMP_SIGNAL", None)
sigdump_path: str = os.getenv("SIGDUMP_PATH", f"/tmp/sigdump-{os.getpid()}.log")


def dump_backtrace(f: 'TextIO', frame: 'FrameType') -> None:
    f.write("  Stacktrace:\n")
    traceback.print_stack(frame, file=f)
    f.write("\n")


def dump_gc_stat(f: 'TextIO') -> None:
    f.write("  GC stat:\n")
    for i, generation in enumerate(gc.get_stats()):
        f.write(f"    Generation {i}:\n")
        f.write(f"      collections   : {generation.get('collections')}\n")
        f.write(f"      collected     : {generation.get('collected')}\n")
        f.write(f"      uncollectable : {generation.get('uncollectable')}\n")


def dump(f: 'TextIO', frame: 'FrameType') -> None:
    f.write(f"Sigdump at {datetime.now()} process {os.getpid()}\n\n")
    dump_backtrace(f, frame)
    dump_gc_stat(f)
    f.flush()


def handler(signum: int, frame: 'FrameType') -> None:
    if sigdump_path == "-":
        dump(sys.stdout, frame)
        return

    if sigdump_path == "+":
        dump(sys.stderr, frame)
        return

    with open(sigdump_path, 'a') as f:
        dump(f, frame)
        return


def enable(verbose: bool = True) -> None:
    signal_no: int = signal.SIGCONT
    if sigdump_signal is not None:
        signal_no = getattr(signal, sigdump_signal.upper())
    signal.signal(signal_no, handler)

    if verbose:
        display_path = sigdump_path
        if display_path == '-':
            display_path = 'stdout'
        elif display_path == '+':
            display_path = 'stderr'
        print(f"SIGDUMP is enabled. The result is exported to {display_path}.")
