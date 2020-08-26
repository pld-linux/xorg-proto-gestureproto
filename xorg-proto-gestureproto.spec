Summary:	Gesture extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia Gesture
Name:		xorg-proto-gestureproto
Version:	0.1.1
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://download.tizen.org/releases/2.4/2.4-mobile/latest/repos/target-TM1/source/xorg-x11-proto-gesture-%{version}-1.1.src.rpm
# Source0-md5:	2785baf642228d1081177bd9251bb0c7
Patch0:		%{name}-c-p.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	rpm-utils
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gesture extension headers.

%description -l pl.UTF-8
Pliki nagłówkowe rozszerzenia Gesture.

%package devel
Summary:	Gesture extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia Gesture
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
Gesture extension headers.

%description devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia Gesture.

%prep
%setup -q -c -T -n xorg-x11-proto-gesture-%{version}
rpm2cpio %{SOURCE0} | cpio -i xorg-x11-proto-gesture-%{version}.tar.gz
tar xf xorg-x11-proto-gesture-%{version}.tar.gz -C ..
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE.MIT NOTICE
%{_includedir}/X11/extensions/gesture*.h
%{_pkgconfigdir}/gestureproto.pc
