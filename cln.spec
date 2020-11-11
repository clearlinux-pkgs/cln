#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cln
Version  : 1.3.6
Release  : 4
URL      : https://www.ginac.de/CLN/cln-1.3.6.tar.bz2
Source0  : https://www.ginac.de/CLN/cln-1.3.6.tar.bz2
Summary  : Class Library for Numbers
Group    : Development/Tools
License  : GPL-2.0
Requires: cln-bin = %{version}-%{release}
Requires: cln-info = %{version}-%{release}
Requires: cln-lib = %{version}-%{release}
Requires: cln-license = %{version}-%{release}
Requires: cln-man = %{version}-%{release}

%description
Class Library for Numbers
GPL
Features:
- Rich set of number classes:
Integer (unlimited precision), rational, short float,
single float, double float, long float (unlimited
precision), complex, modular integer, univariate polynomial.
- Elementary, logical, transcendental functions.
- C++ as implementation language brings
- efficiency,
- type safety,
- algebraic syntax.
- Memory efficiency:
- Small integers and short floats are immediate,
not heap allocated.
- Automatic, non-interruptive garbage collection.
- Speed efficiency:
- Assembly language kernel for some CPUs,
- Karatsuba and Schönhage-Strassen multiplication.
- Interoperability:
- Garbage collection with no burden on
the main application,
- hooks for memory allocation.

%package bin
Summary: bin components for the cln package.
Group: Binaries
Requires: cln-license = %{version}-%{release}

%description bin
bin components for the cln package.


%package dev
Summary: dev components for the cln package.
Group: Development
Requires: cln-lib = %{version}-%{release}
Requires: cln-bin = %{version}-%{release}
Provides: cln-devel = %{version}-%{release}
Requires: cln = %{version}-%{release}

%description dev
dev components for the cln package.


%package info
Summary: info components for the cln package.
Group: Default

%description info
info components for the cln package.


%package lib
Summary: lib components for the cln package.
Group: Libraries
Requires: cln-license = %{version}-%{release}

%description lib
lib components for the cln package.


%package license
Summary: license components for the cln package.
Group: Default

%description license
license components for the cln package.


%package man
Summary: man components for the cln package.
Group: Default

%description man
man components for the cln package.


%prep
%setup -q -n cln-1.3.6
cd %{_builddir}/cln-1.3.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605126864
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1605126864
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cln
cp %{_builddir}/cln-1.3.6/COPYING %{buildroot}/usr/share/package-licenses/cln/9b8afbb8365ddef80760a26c474036d9d81a0cfd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pi

%files dev
%defattr(-,root,root,-)
/usr/include/cln/GV.h
/usr/include/cln/GV_complex.h
/usr/include/cln/GV_integer.h
/usr/include/cln/GV_modinteger.h
/usr/include/cln/GV_number.h
/usr/include/cln/GV_rational.h
/usr/include/cln/GV_real.h
/usr/include/cln/SV.h
/usr/include/cln/SV_complex.h
/usr/include/cln/SV_integer.h
/usr/include/cln/SV_number.h
/usr/include/cln/SV_rational.h
/usr/include/cln/SV_real.h
/usr/include/cln/SV_ringelt.h
/usr/include/cln/V.h
/usr/include/cln/cln.h
/usr/include/cln/complex.h
/usr/include/cln/complex_class.h
/usr/include/cln/complex_io.h
/usr/include/cln/complex_ring.h
/usr/include/cln/condition.h
/usr/include/cln/config.h
/usr/include/cln/dfloat.h
/usr/include/cln/dfloat_class.h
/usr/include/cln/dfloat_io.h
/usr/include/cln/exception.h
/usr/include/cln/ffloat.h
/usr/include/cln/ffloat_class.h
/usr/include/cln/ffloat_io.h
/usr/include/cln/float.h
/usr/include/cln/float_class.h
/usr/include/cln/float_io.h
/usr/include/cln/floatformat.h
/usr/include/cln/host_cpu.h
/usr/include/cln/input.h
/usr/include/cln/integer.h
/usr/include/cln/integer_class.h
/usr/include/cln/integer_io.h
/usr/include/cln/integer_ring.h
/usr/include/cln/intparam.h
/usr/include/cln/io.h
/usr/include/cln/lfloat.h
/usr/include/cln/lfloat_class.h
/usr/include/cln/lfloat_io.h
/usr/include/cln/malloc.h
/usr/include/cln/modinteger.h
/usr/include/cln/modules.h
/usr/include/cln/null_ring.h
/usr/include/cln/number.h
/usr/include/cln/number_io.h
/usr/include/cln/numtheory.h
/usr/include/cln/object.h
/usr/include/cln/output.h
/usr/include/cln/proplist.h
/usr/include/cln/random.h
/usr/include/cln/rational.h
/usr/include/cln/rational_class.h
/usr/include/cln/rational_io.h
/usr/include/cln/rational_ring.h
/usr/include/cln/real.h
/usr/include/cln/real_class.h
/usr/include/cln/real_io.h
/usr/include/cln/real_ring.h
/usr/include/cln/ring.h
/usr/include/cln/sfloat.h
/usr/include/cln/sfloat_class.h
/usr/include/cln/sfloat_io.h
/usr/include/cln/string.h
/usr/include/cln/symbol.h
/usr/include/cln/timing.h
/usr/include/cln/types.h
/usr/include/cln/univpoly.h
/usr/include/cln/univpoly_complex.h
/usr/include/cln/univpoly_integer.h
/usr/include/cln/univpoly_modint.h
/usr/include/cln/univpoly_rational.h
/usr/include/cln/univpoly_real.h
/usr/include/cln/version.h
/usr/lib64/libcln.so
/usr/lib64/pkgconfig/cln.pc

%files info
%defattr(0644,root,root,0755)
/usr/share/info/cln.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcln.so.6
/usr/lib64/libcln.so.6.0.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cln/9b8afbb8365ddef80760a26c474036d9d81a0cfd

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pi.1
