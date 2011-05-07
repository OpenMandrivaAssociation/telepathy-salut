Name:           telepathy-salut
Version:        0.5.0
Release:        %mkrel 1
Summary:        Connection manager implementing link-local messaging for XMPP

Group:          Networking/Instant messaging
License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/%name/%{name}-%version.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  pkgconfig
BuildRequires:  glib2-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  libxml2-devel
BuildRequires:  avahi-gobject-devel
BuildRequires:  libxslt-proc
BuildRequires:  libtelepathy-glib-devel
BuildRequires:  python
BuildRequires:  gtk-doc
BuildRequires:  libsoup-2.4-devel
BuildRequires:  libuuid-devel
Requires:       telepathy-filesystem

%description
telepathy-salut is a connection manager implementing link-local
messaging for XMPP

http://www.xmpp.org/extensions/xep-0174.html

%files
%defattr(-,root,root,-)
%doc docs/clique.xml NEWS README 
%{_libdir}/telepathy-salut
%{_mandir}/man8/telepathy-salut.8.*
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/salut.manager

#--------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --enable-gtk-doc --enable-olpc
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %buildroot%_datadir/%name

%clean
rm -rf %{buildroot}
