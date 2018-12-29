#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jsonpath-rw
Version  : 1.4.0
Release  : 28
URL      : http://pypi.debian.net/jsonpath-rw/jsonpath-rw-1.4.0.tar.gz
Source0  : http://pypi.debian.net/jsonpath-rw/jsonpath-rw-1.4.0.tar.gz
Summary  : A robust and significantly extended implementation of JSONPath for Python, with a clear AST for metaprogramming.
Group    : Development/Tools
License  : Apache-2.0
Requires: jsonpath-rw-bin
Requires: jsonpath-rw-python3
Requires: jsonpath-rw-python
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
Requires: jsonpath-rw-python3

%description python
python components for the jsonpath-rw package.


%package python3
Summary: python3 components for the jsonpath-rw package.
Group: Default
Requires: python3-core

%description python3
python3 components for the jsonpath-rw package.


%prep
%setup -q -n jsonpath-rw-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535065734
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
