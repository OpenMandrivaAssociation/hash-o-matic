Name:           hash-o-matic
Version:        1.0.1
Release:        1
Summary:        Simple hash validator allowing to compare two files, generate the checksum of a file and verify if a hash matches a file.
License:        LGPL-2.1
URL:            https://apps.kde.org/pl/hashomatic/
Source0:        https://download.kde.org/stable/hash-o-matic/hash-o-matic-%{version}.tar.xz

BuildRequires:  cmake ninja git
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KPim6Libkleo)
BuildRequires:  cmake(Gpgmepp)
BuildRequires:  cmake(QGpgmeQt6)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  qt6-qtbase-theme-gtk3

%description
Simple hash validator allowing to compare two files, generate the checksum of a file and verify if a hash matches a file.

%prep
%autosetup -p1
%cmake \
        -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang hashomatic

%files -f hashomatic.lang
%{_bindir}/hashomatic
%{_datadir}/applications/org.kde.hashomatic.desktop
%{_datadir}/kio/servicemenus/hashFile.desktop
%{_datadir}/metainfo/org.kde.hashomatic.metainfo.xml
%{_iconsdir}/hicolor/scalable/apps/org.kde.hashomatic.svg
