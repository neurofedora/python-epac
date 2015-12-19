%global commit0 45e63f254e62e564bad929103d1fff666ab88fef
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global modname epac


Name:          python-%{modname}
Version:       0.0.1
Release:       1.git%{shortcommit0}%{?dist}
Summary:       Embarrassingly Parallel Array Computing: EPAC is a machine learning workflow builder

License:       BSD 3-Clause
URL:           https://github.com/neurospin/pylearn-%{modname}
Source0:       %{url}/archive/%{commit0}/.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildArch:     noarch
BuildRequires: python2-devel

%description
Embarrassingly Parallel Array Computing: EPAC is a machine learning
workflow builder.

%prep
%autosetup -n pylearn-%{modname}-%{commit0}

%build
%py2_build

%install
%py2_install

%check
%{__python2} setup.py test

%files
%doc doc README.md
%license LICENSE
%{python2_sitelib}/%{modname}*
%{_bindir}/%{modname}*

%changelog
* Sat Dec 19 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.0.1-1
- Initial package
