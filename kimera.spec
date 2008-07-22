%define version   1.40
%define release   %mkrel 3

Name:      kimera
Summary:   Another input method for Japanese
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPL
URL:       http://kimera.sourceforge.jp/
Source0:   http://prdownloads.sourceforge.jp/kimera/17746/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:        anthy, prime
BuildRequires:   anthy-devel, prime
BuildRequires:   qt3-devel, X11-devel

%description
Kimera is another input method for Japanese.
It supports Anthy.


%prep
%setup -q

%build
qmake "target.path=/usr/lib/kimera" "script.path=/usr/bin" kimera.pro
make clean
make

%install
rm -rf $RPM_BUILD_ROOT

# install bin files
install -d %{buildroot}%{_bindir}
install -m 755 kimera %{buildroot}%{_bindir}

# install lib files
install -d %{buildroot}%{_libdir}/kimera
install -m 755 kimera-bin %{buildroot}%{_libdir}/kimera/
install -d %{buildroot}%{_libdir}/kimera/dic/
install -m 644 dic/*.dic %{buildroot}%{_libdir}/kimera/dic/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc AUTHORS COPYING README*
%{_bindir}/kimera
%{_libdir}/kimera/kimera-bin
%{_libdir}/kimera/dic/*.dic
