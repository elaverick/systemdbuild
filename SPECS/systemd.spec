# Include the original definition of meson macro
%global original_meson %meson

# Redefine the meson macro without --buildtype=plain
%global meson %(echo "%{original_meson}" | sed 's/--buildtype=plain//')

Summary: System and Service Manager
Name: systemd
Version: %{VERSION}
Release: 1%{PKG_RELEASE}
License: LGPLv2+
Source0: v%{VERSION}.tar.gz

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

%build
PKG_CONFIG_PATH="/usr/lib/pkgconfig:/tools/lib/pkgconfig" \
LANG=en_US.UTF-8                   \
%meson \
      --prefix=/usr                \
      --sysconfdir=/etc            \
      --localstatedir=/var         \
      -Dblkid=true                 \
      -Dbuildtype=release          \
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
      -Drpmmacrosdir=no
%meson_build

%install
%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
/etc/systemd