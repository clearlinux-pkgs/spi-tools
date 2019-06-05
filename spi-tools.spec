#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : spi-tools
Version  : 0.8.3
Release  : 6
URL      : https://github.com/cpb-/spi-tools/archive/0.8.3.tar.gz
Source0  : https://github.com/cpb-/spi-tools/archive/0.8.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: spi-tools-bin
Requires: spi-tools-license
Requires: spi-tools-man
BuildRequires : doxygen

%description
spi-tools
=========
This package contains some simple command line tools to help using Linux spidev devices.

%package bin
Summary: bin components for the spi-tools package.
Group: Binaries
Requires: spi-tools-license
Requires: spi-tools-man

%description bin
bin components for the spi-tools package.


%package license
Summary: license components for the spi-tools package.
Group: Default

%description license
license components for the spi-tools package.


%package man
Summary: man components for the spi-tools package.
Group: Default

%description man
man components for the spi-tools package.


%prep
%setup -q -n spi-tools-0.8.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535826606
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1535826606
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/spi-tools
cp LICENSE %{buildroot}/usr/share/doc/spi-tools/LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/spi-config
/usr/bin/spi-pipe

%files license
%defattr(-,root,root,-)
/usr/share/doc/spi-tools/LICENSE

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/spi-config.1
/usr/share/man/man1/spi-pipe.1
