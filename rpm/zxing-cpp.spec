Name:       zxing-cpp
Summary:    ZXing port to C++
Version:    2.0.0
Release:    1
License:    ASL 2.0
URL:        https://github.com/sailfishos/zxing
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.10

%package devel
Summary: Development files for the %{name} package
Requires: %{name} = %{version}-%{release}

%description
ZXing-C++ ("zebra crossing") is an open-source, multi-format 1D/2D barcode image processing library implemented in C++.

%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
%cmake -DBUILD_EXAMPLES=false
%make_build

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license LICENSE
%{_libdir}/libZXing.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/ZXing/*
%{_libdir}/libZXing.so
%{_libdir}/pkgconfig/zxing.pc
%{_libdir}/cmake/ZXing/*.cmake
