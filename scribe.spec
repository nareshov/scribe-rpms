#%define ver 2.2
#wget https:/ /download.github.com/facebook-scribe-2ee14d3.tar.gz
%define ver 20111108

Name:           scribe 
Version:        %{ver}
Release:        kiwi1
Summary:        facebook thrift
Group:          Development/Languages
License:        ERPL
URL:            http://www.mozilla.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source:         http://cloud.github.com/downloads/facebook/scribe/scribe.tar.gz
Patch0:		scribe-aclocal-lib64.patch

BuildRequires:	thrift thrift-fb303 boost141-devel libevent libevent-devel


%description 
facebook scribe

%package python
Summary:        scribe-python
Group:          Development/Languages
%description python
facebook scribe python

%prep
%setup -q -n scribe
%patch0 -p1

%build
rm -rf $RPM_BUILD_ROOT
autoreconf --force --verbose --install
CPPFLAGS=-I%{_includedir}/boost141 \
LDFLAGS=-L%{_libdir}/boost141 \
 ./configure \
 --with-boost=/usr \
 --with-thriftpath=/usr \
 --with-fb303path=/usr \
 --prefix=%{_prefix}
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/lib/*
%exclude /usr/lib/python*
%{_bindir}/*

%files python
/usr/lib/python*
