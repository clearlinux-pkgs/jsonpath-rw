#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jsonpath-rw
Version  : 1.4.0
Release  : 36
URL      : http://pypi.debian.net/jsonpath-rw/jsonpath-rw-1.4.0.tar.gz
Source0  : http://pypi.debian.net/jsonpath-rw/jsonpath-rw-1.4.0.tar.gz
Summary  : A robust and significantly extended implementation of JSONPath for Python, with a clear AST for metaprogramming.
Group    : Development/Tools
License  : Apache-2.0
Requires: jsonpath-rw-bin = %{version}-%{release}
Requires: jsonpath-rw-python = %{version}-%{release}
Requires: jsonpath-rw-python3 = %{version}-%{release}
Requires: decorator
Requires: ply
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : decorator
BuildRequires : ply
BuildRequires : six

%description
==================

%package bin
Summary: bin components for the jsonpath-rw package.
Group: Binaries

%description bin
bin components for the jsonpath-rw package.


%package python
Summary: python components for the jsonpath-rw package.
Group: Default
Requires: jsonpath-rw-python3 = %{version}-%{release}

%description python
python components for the jsonpath-rw package.


%package python3
Summary: python3 components for the jsonpath-rw package.
Group: Default
Requires: python3-core
Provides: pypi(jsonpath_rw)
Requires: pypi(decorator)
Requires: pypi(ply)
Requires: pypi(six)

%description python3
python3 components for the jsonpath-rw package.


%prep
%setup -q -n jsonpath-rw-1.4.0
cd %{_builddir}/jsonpath-rw-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583536284
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jsonpath.py

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
