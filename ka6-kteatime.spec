#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.04.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kteatime
Summary:	kteatime
Summary(pl.UTF-8):	kteatime
Name:		ka6-%{kaname}
Version:	25.04.2
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	23ff1f18e2c6d5610dcb22a7c103df49
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kiconthemes-devel >= %{kframever}
BuildRequires:	kf6-knotifications-devel >= %{kframever}
BuildRequires:	kf6-knotifyconfig-devel >= %{kframever}
BuildRequires:	kf6-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KTeaTime is a handy timer for steeping tea. No longer will you have to
guess at how long it takes for your tea to be ready. Simply select the
type of tea you have, and it will alert you when the tea is ready to
drink.

%description -l pl.UTF-8
KTeaTime jest przydatnym stoperem do zaparzania herbaty. Nie musisz
więcej zgadywać jak długo trzeba czekać aż herbata będzie gotowa.
Po prostu zaznacz typ herbaty którą masz i KTeaTime powiadomi Cię,
gdy napój będzie gotowy do picia.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kteatime
%{_desktopdir}/org.kde.kteatime.desktop
%{_iconsdir}/hicolor/*x*/apps/kteatime.png
%{_iconsdir}/hicolor/scalable/apps/kteatime.svgz
%{_datadir}/knotifications6/kteatime.notifyrc
%{_datadir}/metainfo/org.kde.kteatime.appdata.xml
