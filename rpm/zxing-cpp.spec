Name:       zxing-cpp
Summary:    ZXing port to C++
Version:    3.0.2
Release:    1
License:    ASL 2.0
URL:        https://github.com/sailfishos/zxing
Source0:    %{name}-%{version}.tar.gz
Patch1:     0001-Use-consistent-soname-version.patch
Patch2:     0002-Don-t-clone-stb-during-build.patch
BuildRequires:  cmake >= 3.16

%package devel
Summary: Development files for the %{name} package
Requires: %{name} = %{version}-%{release}

%description
ZXing-C++ ("zebra crossing") is an open-source, multi-format 1D/2D barcode image processing library implemented in C++.

%description devel
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%cmake -DZXING_EXAMPLES=false
%make_build

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE
%{_libdir}/libZXing.so.*

%files devel
%{_includedir}/ZXing/*
%{_libdir}/libZXing.so
%{_libdir}/pkgconfig/zxing.pc
%{_libdir}/cmake/ZXing/*.cmake
