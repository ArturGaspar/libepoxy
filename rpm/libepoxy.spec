Name:       libepoxy
Version:    1.5.10
Release:    1%{?dist}
Summary:    Epoxy is a library for handling OpenGL function pointer management for you
License:    MIT
URL:        https://github.com/anholt/libepoxy
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  ccache
BuildRequires:  meson >= 0.54.0
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv1_cm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(x11)

%description
Epoxy is a library for handling OpenGL function pointer management for
you.

It hides the complexity of dlopen(), dlsym(), glXGetProcAddress(),
eglGetProcAddress(), etc. from the app developer, with very little
knowledge needed on their part. They get to read GL specs and write
code using undecorated function names like glCompileShader().

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
%meson \
    -Dglx=yes \
    -Dtests=false
%meson_build

%install
%meson_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%license COPYING
%{_includedir}/epoxy
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/epoxy.pc
