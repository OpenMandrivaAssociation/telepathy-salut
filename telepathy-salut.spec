%define libdev %mklibname %name -d
%define _disable_ld_no_undefined 1

Name:           telepathy-salut
Version:        0.8.1
Release:        1
Summary:        Connection manager implementing link-local messaging for XMPP

Group:          Networking/Instant messaging
License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/%name/%{name}-%version.tar.gz
Source100:	telepathy-salut.rpmlintrc

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	avahi-gobject-devel
BuildRequires:	pkgconfig(libexslt)
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	python
BuildRequires:	python-twisted
BuildRequires:	avahi-python
BuildRequires:	gtk-doc
BuildRequires:	libsoup-devel
BuildRequires:	pkgconfig(uuid)
BuildRequires:	python-xmldiff
BuildRequires:	pkgconfig(gnutls)
Requires:	telepathy-filesystem

%description
telepathy-salut is a connection manager implementing link-local
messaging for XMPP

http://www.xmpp.org/extensions/xep-0174.html

%files -n %name
%doc docs/clique.xml NEWS README 
#%{_libdir}/telepathy/salut-*/lib/*plugins
%{_libdir}/telepathy/salut-*/*/libsalut-plugins-%version.so
%{_libdir}/telepathy/salut-*/*/libwocky-telepathy-salut-%version.so
%{_libexecdir}/telepathy-salut
%{_mandir}/man8/telepathy-salut.8.*
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/salut.manager

#--------------------------------------------------------------------

%package -n %libdev
Summary:    Header files, libraries and development documentation for %{name}
Group:      Development/C
Requires:   %{name} = %version
Provides:   %{name}-devel = %version-%release

Conflicts:  %name  < 0.8.0-2

%description -n %libdev
This package contains the header files, static libraries and development
documentation for %{name}.
If you like to develop programs using %{name},
you will need to install %{name}-devel.

%files -n %libdev
%_libdir/telepathy/salut-0/lib/libsalut-plugins.so
%_libdir/telepathy/salut-0/lib/libwocky.so

#--------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --enable-gtk-doc --enable-olpc --disable-static
%make

%install
%makeinstall_std

rm -f %buildroot%_datadir/%name
rm -f %buildroot%_libdir/telepathy/salut-0/lib/*.la
