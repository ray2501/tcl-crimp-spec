#
# RPM spec for tcl-crimp
#

%define tarname CRIMP

Name:           tcl-crimp
Version:        0.1
Summary:        C Raster Image Manipulation Package for Tcl
Release:        0
License:        TCL
Group:          Development/Libraries/Tcl
Url:            https://core.tcl.tk/akupries/crimp/home
BuildRequires:  tcl >= 8.5
BuildRequires:  tk >= 8.5
BuildRequires:  critcl
BuildRequires:  critcl-devel
BuildRequires:  tcllib
BuildRequires:  tklib
BuildRequires:  gcc
Requires:       tcl >= 8.5
Requires:       tk >= 8.5
Requires:       tcllib
Requires:       tklib
Source:         %{tarname}-%{version}.tar.gz
Patch0:         plot.tcl.patch
BuildRoot:      %{_tmppath}/%{tarname}-%{version}-build

%description
The C Raster Image Manipulation Package, CRIMP provides image manipulation
and processing commands for Tcl which are mostly independent of Tk.
The only part currently depending on Tk is the import from and export to
Tk photos, necessary for display.

%prep
%setup -q -n %{tarname}-%{version}
%patch0

%build

%install
tclsh ./build.tcl install %{buildroot}%_libdir/tcl

# Remove crimp-core header files
rm -rf %{buildroot}%_libdir/include

%files
%defattr(-,root,root)
%doc NOTES.txt
%_libdir/tcl/crimp0.1
%_libdir/tcl/crimp_bmp0.1
%_libdir/tcl/crimp_core0.1
%_libdir/tcl/crimp_pfm0.1
%_libdir/tcl/crimp_pgm0.1
%_libdir/tcl/crimp_ppm0.1
%_libdir/tcl/crimp_tk0.1

%changelog

