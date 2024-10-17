%define version   2.11
%define release   %mkrel 2

Name:      kimera
Summary:   Another input method for Japanese
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPL
URL:       https://kimera.sourceforge.jp/
Source0:   http://prdownloads.sourceforge.jp/kimera/17746/%{name}-%{version}.tar.gz
Patch0:    kimera-1.40-gcc43.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:        anthy, prime
BuildRequires:   anthy-devel, prime
BuildRequires:   qt4-devel

%description
Kimera is another input method for Japanese.
It supports Anthy.

%prep
%setup -q

%build
%qmake_qt4 target.path="%{_libdir}/%{name}"
%make

%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL_ROOT=%buildroot

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README*
%{_bindir}/kimera
%{_libdir}/kimera
