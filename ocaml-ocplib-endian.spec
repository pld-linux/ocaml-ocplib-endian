#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Optimised OCaml functions to read and write int16/32/64 from strings and bigarrays
Summary(pl.UTF-8):	Zoptymalizowane funkcje OCamla do odczytu i zapisu typów int16/32/64 z typów string i bigarray
Name:		ocaml-ocplib-endian
Version:	1.1
Release:	1
License:	LGPL v2.1 with linking exception
Group:		Libraries
#Source0Download: https://github.com/OCamlPro/ocplib-endian/releases
Source0:	https://github.com/OCamlPro/ocplib-endian/archive/%{version}/ocplib-endian-%{version}.tar.gz
# Source0-md5:	dedf4d69c1b87b3c6c7234f632399285
URL:		https://github.com/OCamlPro/ocplib-endian
BuildRequires:	cppo >= 1.1.0
BuildRequires:	ocaml >= 1:4.02.3
BuildRequires:	ocaml-dune >= 1.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
The library implements three modules:
- EndianString works directly on strings, and provides submodules
  BigEndian and LittleEndian, with their unsafe counter-parts;
- EndianBytes works directly on bytes, and provides submodules
  BigEndian and LittleEndian, with their unsafe counter-parts;
- EndianBigstring works on bigstrings (Bigarrays of chars), and
  provides submodules BigEndian and LittleEndian, with their unsafe
  counter-parts.

This package contains files needed to run bytecode executables using
ocplib-endian library.

%description -l pl.UTF-8
Ta biblioteka implementuje trzy moduły:
- EndianString działa bezpośrednio na łańcuchach i udostępnia
  podmoduły BigEndian oraz LittleEndian wraz z odpowiednikami "unsafe"
- EndianBytes działa bezpośrednio na bajtach i udostępnia podmoduły
  BigEndian oraz LittleEndian wraz z odpowiednikami "unsafe"
- EndianBigstring działa na dużych łańcuchach (Bigarray z elementami
  znakowymi) i udostępnia podmoduły BigEndian oraz LittleEndian wraz z
  odpowiednikami "unsafe"

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ocplib-endian.

%package devel
Summary:	Optimised OCaml functions to read and write int16/32/64 from strings and bigarrays - development part
Summary(pl.UTF-8):	Zoptymalizowane funkcje OCamla do odczytu i zapisu typów int16/32/64 z typów string i bigarray - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
This package contains files needed to develop OCaml programs using
ocplib-endian library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów używających
biblioteki ocplib-endian.

%prep
%setup -q -n ocplib-endian-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ocplib-endian/{,bigstring/}*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ocplib-endian

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md COPYING.txt README.md
%dir %{_libdir}/ocaml/ocplib-endian
%{_libdir}/ocaml/ocplib-endian/META
%{_libdir}/ocaml/ocplib-endian/*.cma
%dir %{_libdir}/ocaml/ocplib-endian/bigstring
%{_libdir}/ocaml/ocplib-endian/bigstring/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ocplib-endian/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ocplib-endian/bigstring/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ocplib-endian/*.cmi
%{_libdir}/ocaml/ocplib-endian/*.cmt
%{_libdir}/ocaml/ocplib-endian/*.cmti
%{_libdir}/ocaml/ocplib-endian/*.mli
%{_libdir}/ocaml/ocplib-endian/bigstring/*.cmi
%{_libdir}/ocaml/ocplib-endian/bigstring/*.cmt
%{_libdir}/ocaml/ocplib-endian/bigstring/*.cmti
%{_libdir}/ocaml/ocplib-endian/bigstring/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ocplib-endian/*.a
%{_libdir}/ocaml/ocplib-endian/*.cmx
%{_libdir}/ocaml/ocplib-endian/*.cmxa
%{_libdir}/ocaml/ocplib-endian/bigstring/*.a
%{_libdir}/ocaml/ocplib-endian/bigstring/*.cmx
%{_libdir}/ocaml/ocplib-endian/bigstring/*.cmxa
%endif
%{_libdir}/ocaml/ocplib-endian/dune-package
%{_libdir}/ocaml/ocplib-endian/opam
