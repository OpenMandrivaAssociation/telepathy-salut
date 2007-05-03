Name:           telepathy-salut
Version:        0.1.2
Release:        %mkrel 2
Summary:        Connection manager implementing link-local messaging for XMPP

Group:          Networking/Instant messaging
License:        LGPL
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  pkgconfig
BuildRequires:  glib2-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  libxml2-devel
BuildRequires:  avahi-glib-devel
BuildRequires:  avahi-client-devel
BuildRequires:  libxslt-proc 
BuildRequires:  telepathy-glib

Requires:	telepathy-filesystem


%description
telepathy-salut is a connection manager implementing link-local 
messaging for XMPP

http://www.xmpp.org/extensions/xep-0174.html


%files
%defattr(-,root,root,-)
%{_bindir}/telepathy-salut
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.salut.service
%{_datadir}/telepathy/managers/salut.manager

#--------------------------------------------------------------------

%prep
%setup -q


%build
%configure --enable-gtk-doc --enable-handle-leak-debug
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT



