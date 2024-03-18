%global debug_package %{nil}

Summary: System and Service Manager
Name: systemd
Version: %{VERSION}
Release: 1%{PKG_RELEASE}
License: LGPLv2+
Source0: v%{VERSION}.tar.gz
Patch0: mesonbuild.patch

# Dependencies
BuildRequires: gcc
BuildRequires: pkgconfig
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: glib2-devel
BuildRequires: libcap-devel
BuildRequires: libselinux-devel

%description
Systemd is a system and service manager for Linux, compatible with SysV and LSB init scripts.

%prep
export PYTHONPATH=/usr/local/lib/python3.9/site-packages/:/usr/local/lib64/python3.9/site-packages/
%setup -q -n %{name}-stable-%{version}
%patch0 -p1

%build
export PYTHONPATH=/usr/local/lib/python3.9/site-packages/:/usr/local/lib64/python3.9/site-packages/
PKG_CONFIG_PATH="/usr/lib/pkgconfig:/tools/lib/pkgconfig" \
LANG=en_US.UTF-8                   \
%__meson \
      --prefix=/usr                \
      --sysconfdir=/etc            \
      --localstatedir=/var         \
      --libdir=%{_libdir} \
      --libexecdir=%{_libexecdir} \
      --bindir=%{_bindir} \
      --sbindir=%{_sbindir} \
      --includedir=%{_includedir} \
      --datadir=%{_datadir} \
      --mandir=%{_mandir} \
      --infodir=%{_infodir} \
      --localedir=%{_datadir}/locale \
      --sysconfdir=%{_sysconfdir} \
      --localstatedir=%{_localstatedir} \
      --sharedstatedir=%{_sharedstatedir} \
      --wrap-mode=%{__meson_wrap_mode} \
      --auto-features=%{__meson_auto_features} \
      -Dblkid=true                 \
      -Dntp-servers='ntp1.npl.co.uk ntp2.npl.co.uk' \
      -Ddns-over-tls='openssl'     \
      -Ddefault-dns-over-tls=yes   \
      -Ddefault-dnssec=yes        \
      -Dbuildtype=release          \
      -Dbpf-framework=true         \
      -Dmode=release               \
      -Ddefault-dnssec=no          \
      -Dfirstboot=false            \
      -Dinstall-tests=false        \
      -Dkmod-path=/bin/kmod        \
      -Dldconfig=false             \
      -Dmount-path=/bin/mount      \
      -Drootprefix=                \
      -Drootlibdir=/lib            \
      -Dsplit-usr=true             \
      -Dsulogin-path=/sbin/sulogin \
      -Dsysusers=false             \
      -Dumount-path=/bin/umount    \
      -Db_lto=false                \
      -Drpmmacrosdir=no            \
      %{_vpath_srcdir} %{_vpath_builddir} \
      %{nil}


%meson_build

%install
%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)


/bin/journalctl
/bin/loginctl
/bin/machinectl
/bin/networkctl
/bin/portablectl
/bin/systemctl
/bin/systemd-ask-password
/bin/systemd-creds
/bin/systemd-escape
/bin/systemd-hwdb
/bin/systemd-inhibit
/bin/systemd-machine-id-setup
/bin/systemd-notify
/bin/systemd-sysext
/bin/systemd-tmpfiles
/bin/systemd-tty-ask-password-agent
/bin/udevadm

# Binfmt
/etc/binfmt.d/

# Init scripts
%doc /etc/init.d/README

# Kernel
/etc/kernel/install.d/

# Sysctl
/etc/sysctl.d/

# Systemd
/etc/systemd/coredump.conf
/etc/systemd/journald.conf
/etc/systemd/logind.conf
/etc/systemd/network/
/etc/systemd/networkd.conf
/etc/systemd/oomd.conf
/etc/systemd/pstore.conf
/etc/systemd/resolved.conf
/etc/systemd/sleep.conf
/etc/systemd/system/
/etc/systemd/system.conf
/etc/systemd/timesyncd.conf
/etc/systemd/user/
/etc/systemd/user.conf

# Tmpfiles
/etc/tmpfiles.d/

# XDG
/etc/xdg/systemd/user

# X11
/etc/X11/xinit/xinitrc.d/50-systemd-user.sh

#lib
/lib/libnss_myhostname.so.2
/lib/libnss_mymachines.so.2
/lib/libnss_resolve.so.2
/lib/libnss_systemd.so.2
/lib/libsystemd.so
/lib/libsystemd.so.0
/lib/libsystemd.so.0.35.0
/lib/libudev.so
/lib/libudev.so.1
/lib/libudev.so.1.7.5

# modprobe.d
%doc /lib/modprobe.d/README
/lib/modprobe.d/systemd.conf

# security
/lib/security/pam_systemd.so

#systemd
/lib/systemd/systemd-update-utmp
/lib/systemd/systemd-reply-password
/lib/systemd/ntp-units.d/80-systemd-timesync.list
/lib/systemd/systemd-hostnamed
/lib/systemd/portable/profile/nonetwork/service.conf
/lib/systemd/portable/profile/default/service.conf
/lib/systemd/portable/profile/trusted/service.conf
/lib/systemd/portable/profile/strict/service.conf
/lib/systemd/systemd-userwork
/lib/systemd/systemd-hibernate-resume
/lib/systemd/systemd-coredump
/lib/systemd/systemd-backlight
/lib/systemd/system-generators/systemd-hibernate-resume-generator
/lib/systemd/system-generators/systemd-sysv-generator
/lib/systemd/system-generators/systemd-rc-local-generator
/lib/systemd/system-generators/systemd-gpt-auto-generator
/lib/systemd/system-generators/systemd-system-update-generator
/lib/systemd/system-generators/systemd-run-generator
/lib/systemd/system-generators/systemd-debug-generator
/lib/systemd/system-generators/systemd-fstab-generator
/lib/systemd/system-generators/systemd-getty-generator
/lib/systemd/systemd-userdbd
/lib/systemd/libsystemd-shared-252.so
/lib/systemd/systemd-initctl
/lib/systemd/systemd-resolved
/lib/systemd/systemd-time-wait-sync
/lib/systemd/systemd-rfkill
/lib/systemd/systemd-vconsole-setup
/lib/systemd/systemd-sysctl
/lib/systemd/systemd-network-generator
/lib/systemd/systemd-makefs
/lib/systemd/systemd-update-done
/lib/systemd/systemd-remount-fs
/lib/systemd/systemd-networkd-wait-online
/lib/systemd/systemd-socket-proxyd
/lib/systemd/systemd-user-runtime-dir
/lib/systemd/system-preset/90-systemd.preset
/lib/systemd/system/runlevel3.target
/lib/systemd/system/multi-user.target.wants/getty.target
/lib/systemd/system/multi-user.target.wants/systemd-update-utmp-runlevel.service
/lib/systemd/system/multi-user.target.wants/systemd-logind.service
/lib/systemd/system/multi-user.target.wants/systemd-user-sessions.service
/lib/systemd/system/multi-user.target.wants/systemd-ask-password-wall.path
/lib/systemd/system/systemd-tmpfiles-clean.service
/lib/systemd/system/local-fs.target.wants/tmp.mount
/lib/systemd/system/getty.target
/lib/systemd/system/user.slice
/lib/systemd/system/rescue.service
/lib/systemd/system/exit.target
/lib/systemd/system/rescue.target.wants/systemd-update-utmp-runlevel.service
/lib/systemd/system/runlevel5.target
/lib/systemd/system/systemd-suspend-then-hibernate.service
/lib/systemd/system/systemd-boot-check-no-failures.service
/lib/systemd/system/quotaon.service
/lib/systemd/system/dbus-org.freedesktop.locale1.service
/lib/systemd/system/graphical.target
/lib/systemd/system/serial-getty@.service
/lib/systemd/system/dbus-org.freedesktop.hostname1.service
/lib/systemd/system/systemd-hostnamed.service
/lib/systemd/system/sound.target
/lib/systemd/system/systemd-journald-dev-log.socket
/lib/systemd/system/dbus-org.freedesktop.machine1.service
/lib/systemd/system/initrd-fs.target
/lib/systemd/system/systemd-localed.service
/lib/systemd/system/systemd-network-generator.service
/lib/systemd/system/systemd-vconsole-setup.service
/lib/systemd/system/smartcard.target
/lib/systemd/system/basic.target
/lib/systemd/system/dev-hugepages.mount
/lib/systemd/system/bluetooth.target
/lib/systemd/system/user@.service.d/10-login-barrier.conf
/lib/systemd/system/graphical.target.wants/systemd-update-utmp-runlevel.service
/lib/systemd/system/swap.target
/lib/systemd/system/user@.service
/lib/systemd/system/systemd-hibernate.service
/lib/systemd/system/machines.target
/lib/systemd/system/sys-fs-fuse-connections.mount
/lib/systemd/system/halt.target
/lib/systemd/system/rpcbind.target
/lib/systemd/system/time-sync.target
/lib/systemd/system/initrd-root-device.target
/lib/systemd/system/runlevel1.target
/lib/systemd/system/rc-local.service
/lib/systemd/system/sleep.target
/lib/systemd/system/multi-user.target
/lib/systemd/system/user-runtime-dir@.service
/lib/systemd/system/systemd-tmpfiles-setup.service
/lib/systemd/system/sockets.target
/lib/systemd/system/systemd-udevd-kernel.socket
/lib/systemd/system/systemd-portabled.service
/lib/systemd/system/emergency.target
/lib/systemd/system/kexec.target
/lib/systemd/system/container-getty@.service
/lib/systemd/system/default.target
/lib/systemd/system/machine.slice
/lib/systemd/system/sys-kernel-config.mount
/lib/systemd/system/systemd-networkd-wait-online.service
/lib/systemd/system/systemd-networkd-wait-online@.service
/lib/systemd/system/initrd-switch-root.service
/lib/systemd/system/systemd-update-utmp-runlevel.service
/lib/systemd/system/suspend-then-hibernate.target
/lib/systemd/system/network.target
/lib/systemd/system/shutdown.target
/lib/systemd/system/user@0.service.d/10-login-barrier.conf
/lib/systemd/system/var-lib-machines.mount
/lib/systemd/system/tmp.mount
/lib/systemd/system/systemd-suspend.service
/lib/systemd/system/dbus-org.freedesktop.login1.service
/lib/systemd/system/sysinit.target.wants/dev-hugepages.mount
/lib/systemd/system/sysinit.target.wants/sys-fs-fuse-connections.mount
/lib/systemd/system/sysinit.target.wants/systemd-tmpfiles-setup.service
/lib/systemd/system/sysinit.target.wants/sys-kernel-config.mount
/lib/systemd/system/sysinit.target.wants/systemd-udev-trigger.service
/lib/systemd/system/sysinit.target.wants/systemd-update-done.service
/lib/systemd/system/sysinit.target.wants/systemd-journal-flush.service
/lib/systemd/system/sysinit.target.wants/systemd-hwdb-update.service
/lib/systemd/system/sysinit.target.wants/systemd-udevd.service
/lib/systemd/system/sysinit.target.wants/systemd-tmpfiles-setup-dev.service
/lib/systemd/system/sysinit.target.wants/proc-sys-fs-binfmt_misc.automount
/lib/systemd/system/sysinit.target.wants/systemd-journal-catalog-update.service
/lib/systemd/system/sysinit.target.wants/dev-mqueue.mount
/lib/systemd/system/sysinit.target.wants/systemd-binfmt.service
/lib/systemd/system/sysinit.target.wants/systemd-machine-id-commit.service
/lib/systemd/system/sysinit.target.wants/systemd-ask-password-console.path
/lib/systemd/system/sysinit.target.wants/systemd-sysctl.service
/lib/systemd/system/sysinit.target.wants/sys-kernel-tracing.mount
/lib/systemd/system/sysinit.target.wants/systemd-random-seed.service
/lib/systemd/system/sysinit.target.wants/systemd-journald.service
/lib/systemd/system/sysinit.target.wants/systemd-update-utmp.service
/lib/systemd/system/sysinit.target.wants/sys-kernel-debug.mount
/lib/systemd/system/sigpwr.target
/lib/systemd/system/systemd-udev-trigger.service
/lib/systemd/system/systemd-journald@.socket
/lib/systemd/system/emergency.service
/lib/systemd/system/systemd-update-done.service
/lib/systemd/system/network-online.target
/lib/systemd/system/rescue.target
/lib/systemd/system/systemd-journal-flush.service
/lib/systemd/system/first-boot-complete.target
/lib/systemd/system/systemd-journald-varlink@.socket
/lib/systemd/system/runlevel6.target
/lib/systemd/system/systemd-logind.service
/lib/systemd/system/systemd-hybrid-sleep.service
/lib/systemd/system/systemd-rfkill.service
/lib/systemd/system/paths.target
/lib/systemd/system/systemd-ask-password-console.service
/lib/systemd/system/remote-fs.target
/lib/systemd/system/getty-pre.target
/lib/systemd/system/systemd-initctl.socket
/lib/systemd/system/nss-user-lookup.target
/lib/systemd/system/systemd-backlight@.service
/lib/systemd/system/systemd-tmpfiles-clean.timer
/lib/systemd/system/suspend.target
/lib/systemd/system/systemd-hibernate-resume@.service
/lib/systemd/system/sockets.target.wants/systemd-journald-dev-log.socket
/lib/systemd/system/sockets.target.wants/systemd-udevd-kernel.socket
/lib/systemd/system/sockets.target.wants/systemd-initctl.socket
/lib/systemd/system/sockets.target.wants/systemd-journald-audit.socket
/lib/systemd/system/sockets.target.wants/systemd-journald.socket
/lib/systemd/system/sockets.target.wants/systemd-udevd-control.socket
/lib/systemd/system/sockets.target.wants/systemd-coredump.socket
/lib/systemd/system/systemd-journald-audit.socket
/lib/systemd/system/systemd-nspawn@.service
/lib/systemd/system/systemd-initctl.service
/lib/systemd/system/systemd-coredump@.service
/lib/systemd/system/initrd-cleanup.service
/lib/systemd/system/systemd-user-sessions.service
/lib/systemd/system/systemd-hwdb-update.service
/lib/systemd/system/initrd-udevadm-cleanup-db.service
/lib/systemd/system/systemd-remount-fs.service
/lib/systemd/system/syslog.socket
/lib/systemd/system/printer.target
/lib/systemd/system/user-.slice.d/10-defaults.conf
/lib/systemd/system/systemd-udevd.service
/lib/systemd/system/runlevel2.target
/lib/systemd/system/systemd-tmpfiles-setup-dev.service
/lib/systemd/system/reboot.target
/lib/systemd/system/proc-sys-fs-binfmt_misc.automount
/lib/systemd/system/systemd-ask-password-wall.service
/lib/systemd/system/systemd-machined.service
/lib/systemd/system/final.target
/lib/systemd/system/systemd-oomd.service
/lib/systemd/system/hybrid-sleep.target
/lib/systemd/system/timers.target
/lib/systemd/system/systemd-journal-catalog-update.service
/lib/systemd/system/systemd-rfkill.socket
/lib/systemd/system/initrd-usr-fs.target
/lib/systemd/system/initrd.target
/lib/systemd/system/initrd-parse-etc.service
/lib/systemd/system/blockdev@.target
/lib/systemd/system/systemd-halt.service
/lib/systemd/system/dbus-org.freedesktop.timedate1.service
/lib/systemd/system/systemd-volatile-root.service
/lib/systemd/system/umount.target
/lib/systemd/system/nss-lookup.target
/lib/systemd/system/systemd-ask-password-wall.path
/lib/systemd/system/remote-fs-pre.target
/lib/systemd/system/systemd-exit.service
/lib/systemd/system/systemd-networkd.socket
/lib/systemd/system/dev-mqueue.mount
/lib/systemd/system/systemd-oomd.socket
/lib/systemd/system/local-fs.target
/lib/systemd/system/boot-complete.target
/lib/systemd/system/time-set.target
/lib/systemd/system/slices.target
/lib/systemd/system/systemd-journald.socket
/lib/systemd/system/systemd-userdbd.service
/lib/systemd/system/system-update.target
/lib/systemd/system/runlevel0.target
/lib/systemd/system/systemd-binfmt.service
/lib/systemd/system/systemd-reboot.service
/lib/systemd/system/timers.target.wants/systemd-tmpfiles-clean.timer
/lib/systemd/system/runlevel4.target
/lib/systemd/system/systemd-machine-id-commit.service
/lib/systemd/system/systemd-networkd.service
/lib/systemd/system/systemd-timesyncd.service
/lib/systemd/system/console-getty.service
/lib/systemd/system/systemd-ask-password-console.path
/lib/systemd/system/systemd-time-wait-sync.service
/lib/systemd/system/factory-reset.target
/lib/systemd/system/local-fs-pre.target
/lib/systemd/system/sysinit.target
/lib/systemd/system/machines.target.wants/var-lib-machines.mount
/lib/systemd/system/systemd-userdbd.socket
/lib/systemd/system/systemd-sysctl.service
/lib/systemd/system/modprobe@.service
/lib/systemd/system/sys-kernel-tracing.mount
/lib/systemd/system/systemd-random-seed.service
/lib/systemd/system/systemd-kexec.service
/lib/systemd/system/proc-sys-fs-binfmt_misc.mount
/lib/systemd/system/systemd-quotacheck.service
/lib/systemd/system/initrd-root-fs.target
/lib/systemd/system/network-pre.target
/lib/systemd/system/dbus-org.freedesktop.portable1.service
/lib/systemd/system/systemd-fsck@.service
/lib/systemd/system/system-update-pre.target
/lib/systemd/system/systemd-sysext.service
/lib/systemd/system/usb-gadget.target
/lib/systemd/system/initrd-switch-root.target
/lib/systemd/system/getty@.service
/lib/systemd/system/debug-shell.service
/lib/systemd/system/systemd-journald.service
/lib/systemd/system/systemd-udev-settle.service
/lib/systemd/system/system-update-cleanup.service
/lib/systemd/system/systemd-timedated.service
/lib/systemd/system/remote-fs.target.wants/var-lib-machines.mount
/lib/systemd/system/hibernate.target
/lib/systemd/system/systemd-journald@.service
/lib/systemd/system/systemd-pstore.service
/lib/systemd/system/systemd-resolved.service
/lib/systemd/system/systemd-poweroff.service
/lib/systemd/system/systemd-fsck-root.service
/lib/systemd/system/poweroff.target
/lib/systemd/system/systemd-update-utmp.service
/lib/systemd/system/systemd-udevd-control.socket
/lib/systemd/system/ctrl-alt-del.target
/lib/systemd/system/autovt@.service
/lib/systemd/system/sys-kernel-debug.mount
/lib/systemd/system/systemd-coredump.socket
/lib/systemd/systemd-logind
/lib/systemd/systemd-binfmt
/lib/systemd/systemd-journald
/lib/systemd/systemd-sysroot-fstab-check
/lib/systemd/systemd
/lib/systemd/systemd-portabled
/lib/systemd/systemd-sleep
/lib/systemd/systemd-xdg-autostart-condition
/lib/systemd/systemd-boot-check-no-failures
/lib/systemd/systemd-sulogin-shell
/lib/systemd/systemd-udevd
/lib/systemd/systemd-quotacheck
/lib/systemd/systemd-user-sessions
/lib/systemd/network/80-wifi-adhoc.network
/lib/systemd/network/80-container-vz.network
/lib/systemd/network/80-wifi-ap.network.example
/lib/systemd/network/80-container-host0.network
/lib/systemd/network/80-ethernet.network.example
/lib/systemd/network/80-6rd-tunnel.network
/lib/systemd/network/99-default.link
/lib/systemd/network/80-wifi-station.network.example
/lib/systemd/network/80-vm-vt.network
/lib/systemd/network/80-container-vb.network
/lib/systemd/network/80-container-ve.network
/lib/systemd/systemd-pstore
/lib/systemd/systemd-machined
/lib/systemd/resolv.conf
/lib/systemd/systemd-cgroups-agent
/lib/systemd/systemd-fsck
/lib/systemd/systemd-ac-power
/lib/systemd/libsystemd-core-252.so
/lib/systemd/systemd-timesyncd
/lib/systemd/systemd-timedated
/lib/systemd/systemd-volatile-root
/lib/systemd/systemd-random-seed
/lib/systemd/systemd-localed
/lib/systemd/systemd-shutdown
/lib/systemd/systemd-networkd
/lib/systemd/systemd-growfs
/lib/systemd/systemd-oomd

# udev
/lib/udev/ata_id
/lib/udev/cdrom_id
/lib/udev/dmi_memory_id
/lib/udev/fido_id
/lib/udev/mtd_probe
/lib/udev/scsi_id
/lib/udev/v4l_id

# udev/hwdb.d
/lib/udev/hwdb.d/20-OUI.hwdb
/lib/udev/hwdb.d/20-acpi-vendor.hwdb
/lib/udev/hwdb.d/20-bluetooth-vendor-product.hwdb
/lib/udev/hwdb.d/20-dmi-id.hwdb
/lib/udev/hwdb.d/20-net-ifname.hwdb
/lib/udev/hwdb.d/20-pci-classes.hwdb
/lib/udev/hwdb.d/20-pci-vendor-model.hwdb
/lib/udev/hwdb.d/20-sdio-classes.hwdb
/lib/udev/hwdb.d/20-sdio-vendor-model.hwdb
/lib/udev/hwdb.d/20-usb-classes.hwdb
/lib/udev/hwdb.d/20-usb-vendor-model.hwdb
/lib/udev/hwdb.d/20-vmbus-class.hwdb
/lib/udev/hwdb.d/60-autosuspend-chromiumos.hwdb
/lib/udev/hwdb.d/60-autosuspend-fingerprint-reader.hwdb
/lib/udev/hwdb.d/60-autosuspend.hwdb
/lib/udev/hwdb.d/60-evdev.hwdb
/lib/udev/hwdb.d/60-input-id.hwdb
/lib/udev/hwdb.d/60-keyboard.hwdb
/lib/udev/hwdb.d/60-seat.hwdb
/lib/udev/hwdb.d/60-sensor.hwdb
/lib/udev/hwdb.d/70-analyzers.hwdb
/lib/udev/hwdb.d/70-av-production.hwdb
/lib/udev/hwdb.d/70-cameras.hwdb
/lib/udev/hwdb.d/70-joystick.hwdb
/lib/udev/hwdb.d/70-mouse.hwdb
/lib/udev/hwdb.d/70-pda.hwdb
/lib/udev/hwdb.d/70-pointingstick.hwdb
/lib/udev/hwdb.d/70-sound-card.hwdb
/lib/udev/hwdb.d/70-touchpad.hwdb
/lib/udev/hwdb.d/80-ieee1394-unit-function.hwdb
%doc /lib/udev/hwdb.d/README

# udev/rules.d
/lib/udev/rules.d/50-udev-default.rules
/lib/udev/rules.d/60-autosuspend.rules
/lib/udev/rules.d/60-block.rules
/lib/udev/rules.d/60-cdrom_id.rules
/lib/udev/rules.d/60-drm.rules
/lib/udev/rules.d/60-evdev.rules
/lib/udev/rules.d/60-fido-id.rules
/lib/udev/rules.d/60-infiniband.rules
/lib/udev/rules.d/60-input-id.rules
/lib/udev/rules.d/60-persistent-alsa.rules
/lib/udev/rules.d/60-persistent-input.rules
/lib/udev/rules.d/60-persistent-storage-tape.rules
/lib/udev/rules.d/60-persistent-storage.rules
/lib/udev/rules.d/60-persistent-v4l.rules
/lib/udev/rules.d/60-sensor.rules
/lib/udev/rules.d/60-serial.rules
/lib/udev/rules.d/64-btrfs.rules
/lib/udev/rules.d/70-camera.rules
/lib/udev/rules.d/70-joystick.rules
/lib/udev/rules.d/70-memory.rules
/lib/udev/rules.d/70-mouse.rules
/lib/udev/rules.d/70-power-switch.rules
/lib/udev/rules.d/70-touchpad.rules
/lib/udev/rules.d/70-uaccess.rules
/lib/udev/rules.d/71-seat.rules
/lib/udev/rules.d/73-seat-late.rules
/lib/udev/rules.d/75-net-description.rules
/lib/udev/rules.d/75-probe_mtd.rules
/lib/udev/rules.d/78-sound-card.rules
/lib/udev/rules.d/80-net-setup-link.rules
/lib/udev/rules.d/81-net-dhcp.rules
/lib/udev/rules.d/90-vconsole.rules
/lib/udev/rules.d/99-systemd.rules
%doc /lib/udev/rules.d/README

# usr
/usr/bin/oomctl
/usr/bin/systemd-detect-virt
/usr/bin/localectl
/usr/bin/systemd-nspawn
/usr/bin/systemd-path
/usr/bin/coredumpctl
/usr/bin/systemd-id128
/usr/bin/systemd-dissect
/usr/bin/kernel-install
/usr/bin/systemd-cgtop
/usr/bin/hostnamectl
/usr/bin/systemd-socket-activate
/usr/bin/systemd-delta
/usr/bin/busctl
/usr/bin/systemd-stdio-bridge
/usr/bin/systemd-umount
/usr/bin/systemd-mount
/usr/bin/systemd-resolve
/usr/bin/userdbctl
/usr/bin/systemd-cgls
/usr/bin/systemd-analyze
/usr/bin/resolvectl
/usr/bin/systemd-run
/usr/bin/timedatectl
/usr/bin/systemd-cat
/usr/lib/tmpfiles.d/tmp.conf
/usr/lib/tmpfiles.d/systemd.conf
/usr/lib/tmpfiles.d/home.conf
/usr/lib/tmpfiles.d/etc.conf
/usr/lib/tmpfiles.d/legacy.conf
/usr/lib/tmpfiles.d/provision.conf
/usr/lib/tmpfiles.d/systemd-tmp.conf
/usr/lib/tmpfiles.d/systemd-resolve.conf
/usr/lib/tmpfiles.d/var.conf
/usr/lib/tmpfiles.d/journal-nocow.conf
/usr/lib/tmpfiles.d/systemd-nologin.conf
/usr/lib/tmpfiles.d/x11.conf
/usr/lib/tmpfiles.d/systemd-nspawn.conf
/usr/lib/tmpfiles.d/systemd-network.conf
/usr/lib/tmpfiles.d/static-nodes-permissions.conf
%doc /usr/lib/tmpfiles.d/README
/usr/lib/tmpfiles.d/systemd-pstore.conf
/usr/lib/tmpfiles.d/portables.conf
/usr/lib/environment.d/99-environment.conf
/usr/lib/systemd/catalog/systemd.sr.catalog
/usr/lib/systemd/catalog/systemd.fr.catalog
/usr/lib/systemd/catalog/systemd.pt_BR.catalog
/usr/lib/systemd/catalog/systemd.catalog
/usr/lib/systemd/catalog/systemd.de.catalog
/usr/lib/systemd/catalog/systemd.be@latin.catalog
/usr/lib/systemd/catalog/systemd.da.catalog
/usr/lib/systemd/catalog/systemd.pl.catalog
/usr/lib/systemd/catalog/systemd.ru.catalog
/usr/lib/systemd/catalog/systemd.bg.catalog
/usr/lib/systemd/catalog/systemd.zh_CN.catalog
/usr/lib/systemd/catalog/systemd.ko.catalog
/usr/lib/systemd/catalog/systemd.hr.catalog
/usr/lib/systemd/catalog/systemd.be.catalog
/usr/lib/systemd/catalog/systemd.it.catalog
/usr/lib/systemd/catalog/systemd.zh_TW.catalog
/usr/lib/systemd/catalog/systemd.hu.catalog
/usr/lib/systemd/user/systemd-tmpfiles-clean.service
/usr/lib/systemd/user/exit.target
/usr/lib/systemd/user/sound.target
/usr/lib/systemd/user/app.slice
/usr/lib/systemd/user/smartcard.target
/usr/lib/systemd/user/basic.target
/usr/lib/systemd/user/xdg-desktop-autostart.target
/usr/lib/systemd/user/bluetooth.target
/usr/lib/systemd/user/systemd-tmpfiles-setup.service
/usr/lib/systemd/user/sockets.target
/usr/lib/systemd/user/default.target
/usr/lib/systemd/user/shutdown.target
/usr/lib/systemd/user/paths.target
/usr/lib/systemd/user/systemd-tmpfiles-clean.timer
/usr/lib/systemd/user/printer.target
/usr/lib/systemd/user/graphical-session-pre.target
/usr/lib/systemd/user/timers.target
/usr/lib/systemd/user/background.slice
/usr/lib/systemd/user/graphical-session.target
/usr/lib/systemd/user/systemd-exit.service
/usr/lib/systemd/user/session.slice
/usr/lib/systemd/user-environment-generators/30-systemd-environment-d-generator
/usr/lib/systemd/user-preset/90-systemd.preset
/usr/lib/systemd/user-generators/systemd-xdg-autostart-generator
/usr/lib/pam.d/systemd-user
/usr/lib/sysctl.d/50-default.conf
/usr/lib/sysctl.d/50-coredump.conf
%doc /usr/lib/sysctl.d/README
/usr/lib/sysctl.d/50-pid-max.conf
/usr/lib/kernel/install.conf
/usr/lib/kernel/install.d/50-depmod.install
/usr/lib/kernel/install.d/90-loaderentry.install
/usr/include/libudev.h
/usr/include/systemd/sd-journal.h
/usr/include/systemd/sd-messages.h
/usr/include/systemd/sd-hwdb.h
/usr/include/systemd/sd-gpt.h
/usr/include/systemd/sd-path.h
/usr/include/systemd/sd-bus-protocol.h
/usr/include/systemd/sd-device.h
/usr/include/systemd/sd-bus-vtable.h
/usr/include/systemd/sd-event.h
/usr/include/systemd/sd-id128.h
/usr/include/systemd/_sd-common.h
/usr/include/systemd/sd-bus.h
/usr/include/systemd/sd-login.h
/usr/include/systemd/sd-daemon.h
/usr/share/dbus-1/system-services/org.freedesktop.timesync1.service
/usr/share/dbus-1/system-services/org.freedesktop.network1.service
/usr/share/dbus-1/system-services/org.freedesktop.machine1.service
/usr/share/dbus-1/system-services/org.freedesktop.locale1.service
/usr/share/dbus-1/system-services/org.freedesktop.systemd1.service
/usr/share/dbus-1/system-services/org.freedesktop.resolve1.service
/usr/share/dbus-1/system-services/org.freedesktop.oom1.service
/usr/share/dbus-1/system-services/org.freedesktop.portable1.service
/usr/share/dbus-1/system-services/org.freedesktop.login1.service
/usr/share/dbus-1/system-services/org.freedesktop.timedate1.service
/usr/share/dbus-1/system-services/org.freedesktop.hostname1.service
/usr/share/dbus-1/system.d/org.freedesktop.portable1.conf
/usr/share/dbus-1/system.d/org.freedesktop.machine1.conf
/usr/share/dbus-1/system.d/org.freedesktop.hostname1.conf
/usr/share/dbus-1/system.d/org.freedesktop.systemd1.conf
/usr/share/dbus-1/system.d/org.freedesktop.resolve1.conf
/usr/share/dbus-1/system.d/org.freedesktop.oom1.conf
/usr/share/dbus-1/system.d/org.freedesktop.timedate1.conf
/usr/share/dbus-1/system.d/org.freedesktop.locale1.conf
/usr/share/dbus-1/system.d/org.freedesktop.timesync1.conf
/usr/share/dbus-1/system.d/org.freedesktop.login1.conf
/usr/share/dbus-1/system.d/org.freedesktop.network1.conf
/usr/share/dbus-1/services/org.freedesktop.systemd1.service
/usr/share/dbus-1/interfaces/org.freedesktop.locale1.xml
/usr/share/dbus-1/interfaces/org.freedesktop.network1.Manager.xml
/usr/share/dbus-1/interfaces/org.freedesktop.network1.DHCPServer.xml
/usr/share/dbus-1/interfaces/org.freedesktop.systemd1.Service.xml
/usr/share/dbus-1/interfaces/org.freedesktop.login1.Manager.xml
/usr/share/dbus-1/interfaces/org.freedesktop.systemd1.Path.xml
/usr/share/dbus-1/interfaces/org.freedesktop.systemd1.Timer.xml
/usr/share/dbus-1/interfaces/org.freedesktop.LogControl1.xml
/usr/share/dbus-1/interfaces/org.freedesktop.machine1.Machine.xml
/usr/share/dbus-1/interfaces/org.freedesktop.login1.Session.xml
/usr/share/dbus-1/interfaces/org.freedesktop.login1.Seat.xml
/usr/share/dbus-1/interfaces/org.freedesktop.systemd1.Swap.xml
/usr/share/dbus-1/interfaces/org.freedesktop.systemd1.Device.xml
/usr/share/dbus-1/interfaces/org.freedesktop.hostname1.xml
/usr/share/dbus-1/interfaces/org.freedesktop.resolve1.Manager.xml
/usr/share/dbus-1/interfaces/org.freedesktop.oom1.Manager.xml
/usr/share/dbus-1/interfaces/org.freedesktop.systemd1.Scope.xml
/usr/share/dbus-1/interfaces/org.freedesktop.resolve1.Link.xml
/usr/share/dbus-1/interfaces/org.freedesktop.machine1.Manager.xml
/usr/share/dbus-1/interfaces/org.freedesktop.timedate1.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portable1.Image.xml
/usr/share/dbus-1/interfaces/org.freedesktop.systemd1.Socket.xml
/usr/share/dbus-1/interfaces/org.freedesktop.systemd1.Manager.xml
/usr/share/dbus-1/interfaces/org.freedesktop.systemd1.Automount.xml
/usr/share/dbus-1/interfaces/org.freedesktop.login1.User.xml
/usr/share/dbus-1/interfaces/org.freedesktop.network1.Link.xml
/usr/share/dbus-1/interfaces/org.freedesktop.systemd1.Target.xml
/usr/share/dbus-1/interfaces/org.freedesktop.systemd1.Slice.xml
/usr/share/dbus-1/interfaces/org.freedesktop.systemd1.Job.xml
/usr/share/dbus-1/interfaces/org.freedesktop.network1.Network.xml
/usr/share/dbus-1/interfaces/org.freedesktop.systemd1.Mount.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portable1.Manager.xml
/usr/share/dbus-1/interfaces/org.freedesktop.machine1.Image.xml
/usr/share/dbus-1/interfaces/org.freedesktop.systemd1.Unit.xml
/usr/share/dbus-1/interfaces/org.freedesktop.resolve1.DnssdService.xml
/usr/share/bash-completion/completions/oomctl
/usr/share/bash-completion/completions/systemd-detect-virt
/usr/share/bash-completion/completions/systemd-sysext
/usr/share/bash-completion/completions/udevadm
/usr/share/bash-completion/completions/localectl
/usr/share/bash-completion/completions/systemd-nspawn
/usr/share/bash-completion/completions/journalctl
/usr/share/bash-completion/completions/networkctl
/usr/share/bash-completion/completions/systemd-path
/usr/share/bash-completion/completions/coredumpctl
/usr/share/bash-completion/completions/systemd-id128
/usr/share/bash-completion/completions/systemd-dissect
/usr/share/bash-completion/completions/kernel-install
/usr/share/bash-completion/completions/systemd-cgtop
/usr/share/bash-completion/completions/portablectl
/usr/share/bash-completion/completions/hostnamectl
/usr/share/bash-completion/completions/systemd-delta
/usr/share/bash-completion/completions/busctl
/usr/share/bash-completion/completions/systemd-resolve
/usr/share/bash-completion/completions/systemd-cgls
/usr/share/bash-completion/completions/systemd-analyze
/usr/share/bash-completion/completions/machinectl
/usr/share/bash-completion/completions/systemctl
/usr/share/bash-completion/completions/resolvectl
/usr/share/bash-completion/completions/loginctl
/usr/share/bash-completion/completions/systemd-run
/usr/share/bash-completion/completions/timedatectl
/usr/share/bash-completion/completions/systemd-cat
/usr/share/systemd/language-fallback-map
/usr/share/systemd/kbd-model-map
/usr/share/pkgconfig/udev.pc
/usr/share/pkgconfig/systemd.pc
/usr/share/zsh/site-functions/_sd_machines
/usr/share/zsh/site-functions/_hostnamectl
/usr/share/zsh/site-functions/_sd_outputmodes
/usr/share/zsh/site-functions/_machinectl
/usr/share/zsh/site-functions/_coredumpctl
/usr/share/zsh/site-functions/_systemctl
/usr/share/zsh/site-functions/_systemd-nspawn
/usr/share/zsh/site-functions/_localectl
/usr/share/zsh/site-functions/_kernel-install
/usr/share/zsh/site-functions/_systemd-tmpfiles
/usr/share/zsh/site-functions/_systemd-run
/usr/share/zsh/site-functions/_timedatectl
/usr/share/zsh/site-functions/_sd_hosts_or_user_at_host
/usr/share/zsh/site-functions/_journalctl
/usr/share/zsh/site-functions/_systemd
/usr/share/zsh/site-functions/_loginctl
/usr/share/zsh/site-functions/_systemd-inhibit
/usr/share/zsh/site-functions/_systemd-analyze
/usr/share/zsh/site-functions/_oomctl
/usr/share/zsh/site-functions/_resolvectl
/usr/share/zsh/site-functions/_sd_unit_files
/usr/share/zsh/site-functions/_systemd-delta
/usr/share/zsh/site-functions/_systemd-path
/usr/share/zsh/site-functions/_busctl
/usr/share/zsh/site-functions/_networkctl
/usr/share/zsh/site-functions/_udevadm
/usr/share/factory/etc/nsswitch.conf
/usr/share/factory/etc/locale.conf
/usr/share/factory/etc/issue
/usr/share/factory/etc/pam.d/other
/usr/share/factory/etc/pam.d/system-auth
/usr/share/locale/fr/LC_MESSAGES/systemd.mo
/usr/share/locale/pt_BR/LC_MESSAGES/systemd.mo
/usr/share/locale/hu/LC_MESSAGES/systemd.mo
/usr/share/locale/ru/LC_MESSAGES/systemd.mo
/usr/share/locale/sk/LC_MESSAGES/systemd.mo
/usr/share/locale/ca/LC_MESSAGES/systemd.mo
/usr/share/locale/el/LC_MESSAGES/systemd.mo
/usr/share/locale/nl/LC_MESSAGES/systemd.mo
/usr/share/locale/it/LC_MESSAGES/systemd.mo
/usr/share/locale/pa/LC_MESSAGES/systemd.mo
/usr/share/locale/cs/LC_MESSAGES/systemd.mo
/usr/share/locale/si/LC_MESSAGES/systemd.mo
/usr/share/locale/be@latin/LC_MESSAGES/systemd.mo
/usr/share/locale/hr/LC_MESSAGES/systemd.mo
/usr/share/locale/ko/LC_MESSAGES/systemd.mo
/usr/share/locale/tr/LC_MESSAGES/systemd.mo
/usr/share/locale/ka/LC_MESSAGES/systemd.mo
/usr/share/locale/zh_CN/LC_MESSAGES/systemd.mo
/usr/share/locale/de/LC_MESSAGES/systemd.mo
/usr/share/locale/zh_TW/LC_MESSAGES/systemd.mo
/usr/share/locale/bg/LC_MESSAGES/systemd.mo
/usr/share/locale/pt/LC_MESSAGES/systemd.mo
/usr/share/locale/gl/LC_MESSAGES/systemd.mo
/usr/share/locale/sv/LC_MESSAGES/systemd.mo
/usr/share/locale/da/LC_MESSAGES/systemd.mo
/usr/share/locale/et/LC_MESSAGES/systemd.mo
/usr/share/locale/pl/LC_MESSAGES/systemd.mo
/usr/share/locale/uk/LC_MESSAGES/systemd.mo
/usr/share/locale/ja/LC_MESSAGES/systemd.mo
/usr/share/locale/es/LC_MESSAGES/systemd.mo
/usr/share/locale/be/LC_MESSAGES/systemd.mo
/usr/share/locale/ro/LC_MESSAGES/systemd.mo
/usr/share/locale/lt/LC_MESSAGES/systemd.mo
/usr/share/locale/fi/LC_MESSAGES/systemd.mo
/usr/share/locale/sr/LC_MESSAGES/systemd.mo
/usr/share/locale/kab/LC_MESSAGES/systemd.mo
/usr/share/locale/id/LC_MESSAGES/systemd.mo
/usr/share/doc/systemd/DISTRO_PORTING.md
/usr/share/doc/systemd/CODING_STYLE.md
/usr/share/doc/systemd/LICENSE.LGPL2.1
/usr/share/doc/systemd/README.logs
/usr/share/doc/systemd/UIDS-GIDS.md
/usr/share/doc/systemd/TRANSIENT-SETTINGS.md
/usr/share/doc/systemd/ENVIRONMENT.md
/usr/share/doc/systemd/NEWS
%doc /usr/share/doc/systemd/README
/usr/share/doc/systemd/LICENSES/lookup3-public-domain.txt
/usr/share/doc/systemd/LICENSES/murmurhash2-public-domain.txt
/usr/share/doc/systemd/LICENSES/Linux-syscall-note.txt
/usr/share/doc/systemd/LICENSES/CC0-1.0.txt
/usr/share/doc/systemd/LICENSES/OFL-1.1.txt
/usr/share/doc/systemd/LICENSES/BSD-2-Clause.txt
/usr/share/doc/systemd/LICENSES/BSD-3-Clause.txt
/usr/share/doc/systemd/LICENSES/MIT.txt
/usr/share/doc/systemd/LICENSES/README.md
/usr/share/doc/systemd/LICENSES/LGPL-2.0-or-later.txt
/usr/share/doc/systemd/LICENSES/MIT-0.txt
/usr/share/doc/systemd/HACKING.md
/usr/share/doc/systemd/LICENSE.GPL2
/usr/share/doc/systemd/TRANSLATORS.md
/usr/share/polkit-1/rules.d/systemd-networkd.rules
/usr/share/polkit-1/actions/org.freedesktop.systemd1.policy
/usr/share/polkit-1/actions/org.freedesktop.network1.policy
/usr/share/polkit-1/actions/org.freedesktop.login1.policy
/usr/share/polkit-1/actions/org.freedesktop.timedate1.policy
/usr/share/polkit-1/actions/org.freedesktop.machine1.policy
/usr/share/polkit-1/actions/org.freedesktop.portable1.policy
/usr/share/polkit-1/actions/org.freedesktop.hostname1.policy
/usr/share/polkit-1/actions/org.freedesktop.locale1.policy
/usr/share/polkit-1/actions/org.freedesktop.timesync1.policy
/usr/share/polkit-1/actions/org.freedesktop.resolve1.policy
/usr/lib64/pkgconfig/libsystemd.pc
/usr/lib64/pkgconfig/libudev.pc

# sbin
/sbin/telinit
/sbin/poweroff
/sbin/halt
/sbin/init
/sbin/shutdown
/sbin/resolvconf
/sbin/runlevel
/sbin/reboot

# var
/var/lib/systemd
/var/log/journal