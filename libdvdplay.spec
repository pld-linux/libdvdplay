Summary:	libdvdplay - simple library designed for DVD navigation
Summary(pl):	libdvdplay - prosta biblioteka do nawigacji po DVD
Name:		libdvdplay
Version:	1.0.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://download.videolan.org/pub/videolan/libdvdplay/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	602bca4ef78d79aa87e5e8920d958a78
URL:		http://developers.videolan.org/libdvdplay/
BuildRequires:	automake
BuildRequires:	libdvdread-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdvdplay is a portable abstraction library for DVD menus support, it
provides a simple API to access a DVD device as a block device.

%description -l pl
libdvdplay to przeno�na biblioteka abstrakcji do obs�ugi menu DVD.
Udost�pnia proste API do dost�pu do urz�dzenia DVD jako urz�dzenia
blokowego.

%package devel
Summary:	Header files for libdvdplay library
Summary(pl):	Pliki nag��wkowe biblioteki libdvdplay
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libdvdread-devel

%description devel
Header files for libdvdplay library.

%description devel -l pl
Pliki nag��wkowe biblioteki libdvdplay.

%package static
Summary:	Static libdvdplay library
Summary(pl):	Statyczna biblioteka libdvdplay
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libdvdplay library.

%description static -l pl
Statyczna biblioteka libdvdplay.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/libdvdplay.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdvdplay.so
%{_libdir}/libdvdplay.la
%{_includedir}/dvdplay

%files static
%defattr(644,root,root,755)
%{_libdir}/libdvdplay.a
