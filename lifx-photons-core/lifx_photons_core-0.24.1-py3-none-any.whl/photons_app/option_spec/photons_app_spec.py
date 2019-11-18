"""
Here we define the yaml specification for photons_app options and task options

The specifications are responsible for sanitation, validation and normalisation.
"""

from photons_app.registers import TargetRegister, Target, ReferenceResolerRegister
from photons_app.formatter import MergedOptionStringFormatter
from photons_app.errors import BadOption
from photons_app import helpers as hp

from delfick_project.norms import sb, dictobj, va
import asyncio
import logging
import signal
import json
import sys

log = logging.getLogger("photons_app.options_spec.photons_app-spec")


class PhotonsApp(dictobj.Spec):
    """
    The main photons_app object.

    .. dictobj_params::
    """

    config = dictobj.Field(
        sb.file_spec, wrapper=sb.optional_spec, help="The root configuration file"
    )
    extra = dictobj.Field(
        sb.string_spec, default="", help="The arguments after the ``--`` in the commandline"
    )
    debug = dictobj.Field(sb.boolean, default=False, help="Whether we are in debug mode or not")
    target = dictobj.Field(
        wrapper=sb.optional_spec,
        format_into=sb.string_spec,
        help="The target to use when executing the task",
    )
    artifact = dictobj.Field(
        default="", format_into=sb.string_spec, help="The artifact string from the commandline"
    )
    reference = dictobj.Field(
        default="", format_into=sb.string_spec, help="The device(s) to send commands to"
    )
    extra_files = dictobj.Field(sb.string_spec, wrapper=sb.listof, help="Extra files to load")
    chosen_task = dictobj.Field(
        default="list_tasks", format_into=sb.string_spec, help="The task that is being executed"
    )
    cleaners = dictobj.Field(
        lambda: sb.overridden([]),
        help="A list of functions to call when cleaning up at the end of the program",
    )
    default_activate_all_modules = dictobj.Field(
        sb.boolean,
        default=False,
        help="The collector looks at this to determine if we should default to activating all photons modules",
    )

    @hp.memoized_property
    def final_future(self):
        return self.loop.create_future()

    @hp.memoized_property
    def loop(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        if self.debug:
            loop.set_debug(True)
        return loop

    @hp.memoized_property
    def extra_as_json(self):
        options = "{}" if self.extra in (None, "", sb.NotSpecified) else self.extra
        try:
            return json.loads(options)
        except (TypeError, ValueError) as error:
            raise BadOption("The options after -- wasn't valid json", error=error)

    def separate_final_future(self, sleep=0):
        other_future = asyncio.Future()

        def stop():
            other_future.cancel()

        self.loop.remove_signal_handler(signal.SIGTERM)
        self.loop.add_signal_handler(signal.SIGTERM, stop)

        class CM:
            async def __aenter__(s):
                return other_future

            async def __aexit__(s, exc_typ, exc, tb):
                if sleep > 0:
                    await asyncio.sleep(sleep)
                self.final_future.cancel()

        return CM()

    async def cleanup(self, targets):
        for cleaner in self.cleaners:
            try:
                await cleaner()
            except asyncio.CancelledError:
                break
            except KeyboardInterrupt:
                break
            except (RuntimeWarning, Exception):
                exc_info = sys.exc_info()
                log.error(exc_info[1], exc_info=exc_info)

        for target in targets:
            try:
                if hasattr(target, "finish"):
                    await target.finish()
            except asyncio.CancelledError:
                break
            except KeyboardInterrupt:
                break
            except (RuntimeWarning, Exception):
                exc_info = sys.exc_info()
                log.error(exc_info[1], exc_info=exc_info)


class PhotonsAppSpec(object):
    """Knows about photons_app specific configuration"""

    @hp.memoized_property
    def target_name_spec(self):
        """Just needs to be ascii"""
        return sb.valid_string_spec(va.no_whitespace(), va.regexed(r"^[a-zA-Z][a-zA-Z0-9-_\.]*$"))

    @hp.memoized_property
    def photons_app_spec(self):
        """
        Get us an instance of PhotonsApp:

        .. autoclass:: photons_app.option_spec.photons_app_spec.PhotonsApp
        """
        return PhotonsApp.FieldSpec(formatter=MergedOptionStringFormatter)

    @hp.memoized_property
    def target_register_spec(self):
        """
        Make a TargetRegister object

        .. autoclass:: photons_app.option_spec.photons_app_spec.TargetRegister
        """
        return sb.create_spec(
            TargetRegister,
            collector=sb.formatted(
                sb.overridden("{collector}"), formatter=MergedOptionStringFormatter
            ),
        )

    @hp.memoized_property
    def reference_resolver_register_spec(self):
        """
        Make a ReferenceResolerRegister object

        .. autoclass:: photons_app.option_spec.photons_app_spec.ReferenceResolerRegister
        """
        return sb.create_spec(ReferenceResolerRegister)

    @hp.memoized_property
    def targets_spec(self):
        """
        Get us a dictionary of target name to Target object

        .. autoclass:: photons_app.option_spec.photons_app_spec.Target
        """
        return sb.dictof(
            self.target_name_spec, Target.FieldSpec(formatter=MergedOptionStringFormatter)
        )
