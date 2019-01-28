%define __debug_package %{nil}
%global buildid 20190201
%global versionid 2.1

Name:		hunspell-hr
Version:	%{versionid}
Release:	%{buildid}
Epoch:		1
Summary:	Croatian hunspell dictionaries

License:	GPL 2.0/LGPL 2.1/MPL 1.1
URL:		https://www.github.com/krunose/hunspel-hr
Source0:	%{name}-%{versionid}-%{buildid}.tar.gz

Requires:	hunspell
BuildArch:	noarch

%description
Croatian hunspell dictionaries.

%prep
%setup -q -n hunspell-hr
%build
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/myspell
cp -p hr_HR.aff hr_HR.dic $RPM_BUILD_ROOT/usr/share/myspell/

%files
%doc README_hr_HR.txt
%{_datadir}/myspell/*

%changelog
* Fri Feb 01 2019 Ante Smolcic %{versionid}
 - Hyphen discarded. Wordlist updated.
