%define libdev %mklibname %name -d
%define _disable_ld_no_undefined 1

Name:		telepathy-salut
Version:	0.8.1
Release:	13
Summary:	Connection manager implementing link-local messaging for XMPP
Group:		Networking/Instant messaging
License:	LGPLv2+
URL:		https://telepathy.freedesktop.org/wiki/
Source0:	http://telepathy.freedesktop.org/releases/%name/%{name}-%version.tar.gz
Source100:	telepathy-salut.rpmlintrc
Patch0:		https://abf.io/import/telepathy-salut/raw/rosa2021.1/telepathy-salut-0.8.1-python3-syntax.patch
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	avahi-gobject-devel
BuildRequires:	pkgconfig(libexslt)
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	python2
BuildRequires:	python2-twisted
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

%files -n %{name}
%doc docs/clique.xml docs/clique.html NEWS README
#%{_libdir}/telepathy/salut-*/lib/*plugins
%{_libdir}/telepathy/salut-*/*/libsalut-plugins-%version.so
%{_libdir}/telepathy/salut-*/*/libwocky-telepathy-salut-%version.so
%{_libexecdir}/telepathy-salut
%doc %{_mandir}/man8/telepathy-salut.8.*
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/salut.manager

#--------------------------------------------------------------------

%package -n %{libdev}
Summary:	Header files, libraries and development documentation for %{name}
Group:		Development/C
Requires:	%{name} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	%{name}  < 0.8.0-2

%description -n %{libdev}
This package contains the header files, static libraries and development
documentation for %{name}.
If you like to develop programs using %{name},
you will need to install %{name}-devel.

%files -n %{libdev}
%{_libdir}/telepathy/salut-0/lib/libsalut-plugins.so
%{_libdir}/telepathy/salut-0/lib/libwocky.so

#--------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure \
	--enable-gtk-doc \
	--enable-olpc \
	--disable-avahi-tests

%make_build

%install
%make_install

rm -f %{buildroot}%{_datadir}/%{name}
rm -f %{buildroot}%{_libdir}/telepathy/salut-0/lib/*.la
