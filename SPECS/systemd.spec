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
%setup -q -n %{name}-stable-%{version}
%patch0 -p1

%build
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
%doc README
/etc/systemd