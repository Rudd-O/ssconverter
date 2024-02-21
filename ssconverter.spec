# See https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_example_spec_file

%define debug_package %{nil}

%define mybuildnumber %{?build_number}%{?!build_number:1}

Name:           ssconverter
Version:        0.1.3
Release:        %{mybuildnumber}%{?dist}
Summary:        A program to convert to CSV specific sheets of an OpenOffice / LibreOffice spreadsheet

License:        LGPLv2.1+
Source:         %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

Requires:       libreoffice-pyuno

%global _description %{expand:
Tools to find cycles in dot (Graphviz) file formats.}

%description %_description

%prep
%autosetup -p1 -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files %{name}


%check
# no percent tox, pyproject_buildrequires not -t
true


# Note that there is no %%files section for
# the unversioned python module, python-pello.

# For python3-pello, %%{pyproject_files} handles code files and %%license,
# but executables and documentation must be listed in the spec file:

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/%{name}

%changelog
* Wed Feb 21 2024 Manuel Amador <rudd-o@rudd-o.com> 0.1.3-1
- First RPM packaging release
