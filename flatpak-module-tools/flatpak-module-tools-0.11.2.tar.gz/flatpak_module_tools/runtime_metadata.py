import click

@click.option('--name', required=True)
@click.option('--runtime', required=True)
@click.option('--sdk', required=True)
def _finish():

def write_runtime_metadata(name=None,
                           runtime=None,
                           sdk=None,
                           finish_args):
    args = [
        '--name', name,
        '--runtime', runtime,
        '--sdk', sdk,
    ] + finish_args


          --command=COMMAND
           The command to use. If this option is not specified, the first executable found in files/bin is used.

           Note that the command is used when the application is run via flatpak run, and does not affect what gets executed when the
           application is run in other ways, e.g. via the desktop file or D-Bus activation.

       --require-version=MAJOR.MINOR.MICRO
           Require this version of later of flatpak to install/update to this build.

       --share=SUBSYSTEM
           Share a subsystem with the host session. This updates the [Context] group in the metadata. SUBSYSTEM must be one of: network, ipc.
           This option can be used multiple times.

       --unshare=SUBSYSTEM
           Don't share a subsystem with the host session. This updates the [Context] group in the metadata. SUBSYSTEM must be one of: network,
           ipc. This option can be used multiple times.

       --socket=SOCKET
           Expose a well-known socket to the application. This updates the [Context] group in the metadata. SOCKET must be one of: x11,
           wayland, fallback-x11, pulseaudio, system-bus, session-bus, ssh-auth, pcsc. This option can be used multiple times.

           The fallback-x11 option makes the X11 socket available only if there is no Wayland socket. This option was introduced in 0.11.3. To
           support older Flatpak releases, specify both x11 and fallback-x11. The fallback-x11 option takes precedence when both are
           supported.

       --nosocket=SOCKET
           Don't expose a well known socket to the application. This updates the [Context] group in the metadata. SOCKET must be one of: x11,
           wayland, fallback-x11, pulseaudio, system-bus, session-bus, ssh-auth, pcsc. This option can be used multiple times.

       --device=DEVICE
           Expose a device to the application. This updates the [Context] group in the metadata. DEVICE must be one of: dri, kvm, all. This
           option can be used multiple times.

       --nodevice=DEVICE
           Don't expose a device to the application. This updates the [Context] group in the metadata. DEVICE must be one of: dri, kvm, all.
           This option can be used multiple times.

       --allow=FEATURE
           Allow access to a specific feature. This updates the [Context] group in the metadata. FEATURE must be one of: devel, multiarch,
           bluetooth, canbus. This option can be used multiple times.

           The devel feature allows the application to access certain syscalls such as ptrace(), and perf_event_open().

           The multiarch feature allows the application to execute programs compiled for an ABI other than the one supported natively by the
           system. For example, for the x86_64 architecture, 32-bit x86 binaries will be allowed as well.

           The bluetooth feature allows the application to use bluetooth (AF_BLUETOOTH) sockets. Note, for bluetooth to fully work you must
           also have network access.

           The canbus feature allows the application to use canbus (AF_CAN) sockets. Note, for this work you must also have network access.

       --disallow=FEATURE
           Disallow access to a specific feature. This updates the [Context] group in the metadata. FEATURE must be one of: devel, multiarch,
           bluetooth, canbus. This option can be used multiple times.

       --filesystem=FS
           Allow the application access to a subset of the filesystem. This updates the [Context] group in the metadata. FS can be one of:
           home, host, xdg-desktop, xdg-documents, xdg-download, xdg-music, xdg-pictures, xdg-public-share, xdg-templates, xdg-videos,
           xdg-run, xdg-config, xdg-cache, xdg-data, an absolute path, or a homedir-relative path like ~/dir or paths relative to the xdg
           dirs, like xdg-download/subdir. The optional :ro suffix indicates that the location will be read-only. The optional :create suffix
           indicates that the location will be read-write and created if it doesn't exist. This option can be used multiple times.

       --nofilesystem=FILESYSTEM
           Remove access to the specified subset of the filesystem from the application. This overrides to the Context section from the
           application metadata. FILESYSTEM can be one of: home, host, xdg-desktop, xdg-documents, xdg-download, xdg-music, xdg-pictures,
           xdg-public-share, xdg-templates, xdg-videos, an absolute path, or a homedir-relative path like ~/dir. This option can be used
           multiple times.

       --add-policy=SUBSYSTEM.KEY=VALUE
           Add generic policy option. For example, "--add-policy=subsystem.key=v1 --add-policy=subsystem.key=v2" would map to this metadata:

               [Policy subsystem]
               key=v1;v2;

           This option can be used multiple times.

       --remove-policy=SUBSYSTEM.KEY=VALUE
           Remove generic policy option. This option can be used multiple times.

       --env=VAR=VALUE
           Set an environment variable in the application. This updates the [Environment] group in the metadata. This overrides to the Context
           section from the application metadata. This option can be used multiple times.

       --own-name=NAME
           Allow the application to own the well known name NAME on the session bus. If NAME ends with .*, it allows the application to own
           all matching names. This updates the [Session Bus Policy] group in the metadata. This option can be used multiple times.

       --talk-name=NAME
           Allow the application to talk to the well known name NAME on the session bus. If NAME ends with .*, it allows the application to
           talk to all matching names. This updates the [Session Bus Policy] group in the metadata. This option can be used multiple times.

       --system-own-name=NAME
           Allow the application to own the well known name NAME on the system bus. If NAME ends with .*, it allows the application to own all
           matching names. This updates the [System Bus Policy] group in the metadata. This option can be used multiple times.

       --system-talk-name=NAME
           Allow the application to talk to the well known name NAME on the system bus. If NAME ends with .*, it allows the application to
           talk to all matching names. This updates the [System Bus Policy] group in the metadata. This option can be used multiple times.

                  --system-own-name=NAME
           Allow the application to own the well known name NAME on the system bus. If NAME ends with .*, it allows the application to own all
           matching names. This updates the [System Bus Policy] group in the metadata. This option can be used multiple times.

       --system-talk-name=NAME
           Allow the application to talk to the well known name NAME on the system bus. If NAME ends with .*, it allows the application to
           talk to all matching names. This updates the [System Bus Policy] group in the metadata. This option can be used multiple times.

       --persist=FILENAME
           If the application doesn't have access to the real homedir, make the (homedir-relative) path FILENAME a bind mount to the
           corresponding path in the per-application directory, allowing that location to be used for persistent data. This updates the
           [Context] group in the metadata. This option can be used multiple times.

       --runtime=RUNTIME, --sdk=SDK
           Change the runtime or sdk used by the app to the specified partial ref. Unspecified parts of the ref are taken from the old values
           or defaults.

       --metadata=GROUP=KEY[=VALUE]
           Set a generic key in the metadata file. If value is left out it will be set to "true".

       --extension=NAME=VARIABLE[=VALUE]
           Add extension point info. See the documentation for flatpak-metadata(5) for the possible values of VARIABLE and VALUE.

       --remove-extension=NAME
           Remove extension point info.

       --extension-priority=VALUE
           Set the priority (library override order) of the extension point. Only useful for extensions. 0 is the default, and higher value
           means higher priority.

       --extra-data=NAME:SHA256:DOWNLOAD-SIZE:INSTALL-SIZE:URL
           Adds information about extra data uris to the app. These will be downloaded and verified by the client when the app is installed
           and placed in the /app/extra directory. You can also supply an /app/bin/apply_extra script that will be run after the files are
           downloaded.

       --no-exports
           Don't look for exports in the build.

       --no-inherit-permissions
           Don't inherit runtime permissions in the app.

       -v, --verbose
           Print debug information during command processing.

       --ostree-verbose
           Print OSTree debug information during command processing.

