#
# Conditional build:
%bcond_without	static_libs	% don't build static library
#
Summary:	libdvdplay - simple library designed for DVD navigation
Summary(pl.UTF-8):	libdvdplay - prosta biblioteka do nawigacji po DVD
Name:		libdvdplay
Version:	1.0.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://download.videolan.org/pub/videolan/libdvdplay/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	602bca4ef78d79aa87e5e8920d958a78
URL:		http://developers.videolan.org/libdvdplay/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdvdread-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdvdplay is a portable abstraction library for DVD menus support, it
provides a simple API to access a DVD device as a block device.

%description -l pl.UTF-8
libdvdplay to przenośna biblioteka abstrakcji do obsługi menu DVD.
Udostępnia proste API do dostępu do urządzenia DVD jako urządzenia
blokowego.

%package devel
Summary:	Header files for libdvdplay library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdvdplay
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libdvdread-devel

%description devel
Header files for libdvdplay library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libdvdplay.

%package static
Summary:	Static libdvdplay library
Summary(pl.UTF-8):	Statyczna biblioteka libdvdplay
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libdvdplay library.

%description static -l pl.UTF-8
Statyczna biblioteka libdvdplay.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
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

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdvdplay.a
%endif
