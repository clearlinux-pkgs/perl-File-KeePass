#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-KeePass
Version  : 2.03
Release  : 22
URL      : https://cpan.metacpan.org/authors/id/R/RH/RHANDOM/File-KeePass-2.03.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RH/RHANDOM/File-KeePass-2.03.tar.gz
Summary  : Interface to KeePass V1 and V2 database files
Group    : Development/Tools
License  : Artistic-1.0-Perl BSD-3-Clause GPL-1.0 GPL-1.0+ GPL-2.0+ MIT bzip2-1.0.6
Requires: perl-File-KeePass-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Crypt::Rijndael)
BuildRequires : perl(XML::Parser)

%description
NAME
File::KeePass - Interface to KeePass V1 and V2 database files
SYNOPSIS
use File::KeePass;
use Data::Dumper qw(Dumper);

%package dev
Summary: dev components for the perl-File-KeePass package.
Group: Development
Provides: perl-File-KeePass-devel = %{version}-%{release}
Requires: perl-File-KeePass = %{version}-%{release}

%description dev
dev components for the perl-File-KeePass package.


%package perl
Summary: perl components for the perl-File-KeePass package.
Group: Default
Requires: perl-File-KeePass = %{version}-%{release}

%description perl
perl components for the perl-File-KeePass package.


%prep
%setup -q -n File-KeePass-2.03
cd %{_builddir}/File-KeePass-2.03

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::KeePass.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
