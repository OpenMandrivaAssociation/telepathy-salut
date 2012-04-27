%define lib_major 0
%define libname %mklibname report-abrt_dbus %{lib_major}




Name:           telepathy-salut
Version:        0.8.0
Release:        1
Summary:        Connection manager implementing link-local messaging for XMPP

Group:          Networking/Instant messaging
License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/%name/%{name}-%version.tar.gz

BuildRequires:  pkgconfig
BuildRequires:  glib2-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  libxml2-devel
BuildRequires:  avahi-gobject-devel
BuildRequires:  libxslt-proc
BuildRequires:  telepathy-glib-devel
BuildRequires:  python
BuildRequires:  gtk-doc
BuildRequires:  libsoup-devel
BuildRequires:  python-twisted
BuildRequires:  libuuid-devel
Requires:       telepathy-filesystem

%description
telepathy-salut is a connection manager implementing link-local
messaging for XMPP

http://www.xmpp.org/extensions/xep-0174.html

%files
%doc docs/clique.xml NEWS README 
%{_libdir}/telepathy-salut
%{_mandir}/man8/telepathy-salut.8.*
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/salut.manager

#--------------------------------------------------------------------

%package -n	%{name}-plugins
Summary:        Plugins for %{name}
Group:          Networking/Instant messaging
Requires:       %{name} = %{version}-%{release}

%description -n %{name}-plugins
Plugins for %{name}


%files -n %{name}-plugins
%{_libname}/telepathy/salut-0/lib/*.0.*


#-------------------------------------------------------------------
%package  -n	%{name}-plugins-devel
Summary:        Plugins for %{name}
Group:          Networking/Instant messaging
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-plugins = %{version}-%{release}

%description -n %{name}-plugins-devel
Devel files for %{name}


%files -n %{name}-plugins-devel
%{_libdir}/telepathy/salut-0/lib/*.so
%{_libdir}/telepathy/salut-0/lib/*.a

%prep
%setup -q

%build
%configure2_5x --enable-gtk-doc --enable-olpc \
	 --disable-avahi-tests
		
%make

%install
%makeinstall_std

rm -f %buildroot%_datadir/%name
