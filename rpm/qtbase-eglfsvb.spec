Name:		qt5-qtbase-eglfsvb
Version:	0.2+git546c7d785f
Release:	1%{?dist}
Summary:	Eglfsvb

Group:		Qt/Qt
License:	LGPLv2.1 with exception or GPLv3
URL:		http://qt-project.org
Source0:	%{name}-%{version}.tar.bz2
ExclusiveArch:  %{ix86}

BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5PlatformSupport)
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(mtdev)
BuildRequires:	pkgconfig(glib-2.0)

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.

This contains an extended EGLFS plugin for Virtual Box.

%prep
%setup -q -n %{name}-%{version}/qtbase


%build
export QTDIR=/usr/share/qt5
touch .git
cd src/plugins/platforms/eglfsvb
qmake -qt5

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
cd src/plugins/platforms/eglfsvb

%qmake5_install


%files
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqeglfsvb.so

