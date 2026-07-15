Name:           django-provide
Version:        1.0
Release:        1%{?dist}
Summary:        Dummy package providing python3-django for legacy packages
License:        MIT
Provides:       python3-django = 4.2
Provides:       python3-django >= 4.2

%description
This is a dummy RPM that provides the virtual package 'python3-django'
so that older packages like fts3-monitoring can be installed on EL9.
It does not install any actual files or Django itself.

%files
# No files needed for a pure provide package

%changelog
* Mon Mar 30 2026 Dummy <dummy@example.com> - 1.0-1
- Initial dummy provide package
