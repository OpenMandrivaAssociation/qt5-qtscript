%define api %(echo %{version} |cut -d. -f1)
%define major %api
%define beta beta4

%define qtscript %mklibname qt%{api}script %{major}
%define qtscriptd %mklibname qt%{api}script -d
%define qtscript_p_d %mklibname qt%{api}script-private -d

%define qtscripttools %mklibname qt%{api}scripttools %{major}
%define qtscripttoolsd %mklibname qt%{api}scripttools -d
%define qtscripttools_p_d %mklibname qt%{api}scripttools-private -d

%define _qt5_prefix %{_libdir}/qt%{api}

Name:		qt5-qtscript
Version:	5.15.0
%if "%{beta}" != ""
Release:	0.%{beta}.1
%define qttarballdir qtscript-everywhere-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
%define qttarballdir qtscript-everywhere-src-%{version}
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
Summary:	Qt GUI toolkit
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt.io
BuildRequires:	qmake5 = %{version}
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
# For the Provides: generator
BuildRequires:	cmake >= 3.11.0-1

%description
The QtScript module provides classes for making Qt applications
scriptable.

#------------------------------------------------------------------------------

%package -n	%{qtscripttools}
Summary:	Qt%{api} Component Library
Group:		System/Libraries

%description -n %{qtscripttools}
Qt%{api} Component Library.

The QtScriptTools module provides additional components for applications
that use Qt Script.

%files -n	%{qtscripttools}
%{_qt5_libdir}/libQt5ScriptTools.so.%{api}*

#------------------------------------------------------------------------------

%package -n	%{qtscripttoolsd}
Summary:	Devel files needed to build apps based on QtScriptTools
Group:		Development/KDE and Qt
Requires:	%{qtscripttools} = %version
Requires:	qt5-qtbase-devel = %version

%description -n %{qtscripttoolsd}
Devel files needed to build apps based on QtScriptTools.

%files -n	%{qtscripttoolsd}
%{_qt5_libdir}/libQt5ScriptTools.prl
%{_qt5_libdir}/libQt5ScriptTools.so
%{_qt5_libdir}/pkgconfig/Qt5ScriptTools.pc
%{_qt5_includedir}/QtScriptTools
%exclude %{_qt5_includedir}/QtScriptTools/%version
%{_qt5_libdir}/cmake/Qt5ScriptTools
%{_qt5_prefix}/mkspecs/modules/qt_lib_scripttools.pri

#------------------------------------------------------------------------------

%package -n	%{qtscripttools_p_d}
Summary:	Devel files needed to build apps based on QtScriptTools
Group:		Development/KDE and Qt
Requires:	%{qtscripttoolsd} = %version
Provides:	qt5-qtscripttools-private-devel = %version

%description -n %{qtscripttools_p_d}
Devel files needed to build apps based on QtScriptTools.

%files -n	%{qtscripttools_p_d}
%{_qt5_includedir}/QtScriptTools/%version
%{_qt5_prefix}/mkspecs/modules/qt_lib_scripttools_private.pri

#------------------------------------------------------------------------------

%package -n	%{qtscript}
Summary:	Qt%{api} Component Library
Group:		System/Libraries

%description -n %{qtscript}
Qt%{api} Component Library.

The QtScript module provides classes for making Qt applications 
scriptable.

%files -n	%{qtscript}
%{_qt5_libdir}/libQt5Script.so.%{api}*

#------------------------------------------------------------------------------

%package -n	%{qtscriptd}
Summary:	Devel files needed to build apps based on QtScript
Group:		Development/KDE and Qt
Requires:	%{qtscript} = %version
Requires:	qt5-qtbase-devel = %version

%description -n %{qtscriptd}
Devel files needed to build apps based on QtScript.

%files -n	%{qtscriptd}
%{_qt5_libdir}/libQt5Script.prl
%{_qt5_libdir}/libQt5Script.so
%{_qt5_libdir}/pkgconfig/Qt5Script.pc
%dir %{_qt5_includedir}/QtScript
%{_qt5_includedir}/QtScript/QScriptClass
%{_qt5_includedir}/QtScript/QScriptClassPropertyIterator
%{_qt5_includedir}/QtScript/QScriptContext
%{_qt5_includedir}/QtScript/QScriptContextInfo
%{_qt5_includedir}/QtScript/QScriptContextInfoList
%{_qt5_includedir}/QtScript/QScriptEngine
%{_qt5_includedir}/QtScript/QScriptEngineAgent
%{_qt5_includedir}/QtScript/QScriptExtensionInterface
%{_qt5_includedir}/QtScript/QScriptExtensionPlugin
%{_qt5_includedir}/QtScript/QScriptProgram
%{_qt5_includedir}/QtScript/QScriptString
%{_qt5_includedir}/QtScript/QScriptSyntaxCheckResult
%{_qt5_includedir}/QtScript/QScriptValue
%{_qt5_includedir}/QtScript/QScriptValueIterator
%{_qt5_includedir}/QtScript/QScriptValueList
%{_qt5_includedir}/QtScript/QScriptable
%{_qt5_includedir}/QtScript/QtScript
%{_qt5_includedir}/QtScript/QtScriptVersion
%{_qt5_includedir}/QtScript/QtScriptDepends
%{_qt5_includedir}/QtScript/qscriptable.h
%{_qt5_includedir}/QtScript/qscriptclass.h
%{_qt5_includedir}/QtScript/qscriptclasspropertyiterator.h
%{_qt5_includedir}/QtScript/qscriptcontext.h
%{_qt5_includedir}/QtScript/qscriptcontextinfo.h
%{_qt5_includedir}/QtScript/qscriptengine.h
%{_qt5_includedir}/QtScript/qscriptengineagent.h
%{_qt5_includedir}/QtScript/qscriptextensioninterface.h
%{_qt5_includedir}/QtScript/qscriptextensionplugin.h
%{_qt5_includedir}/QtScript/qscriptprogram.h
%{_qt5_includedir}/QtScript/qscriptstring.h
%{_qt5_includedir}/QtScript/qscriptvalue.h
%{_qt5_includedir}/QtScript/qscriptvalueiterator.h
%{_qt5_includedir}/QtScript/qtscript-config.h
%{_qt5_includedir}/QtScript/qtscriptglobal.h
%{_qt5_includedir}/QtScript/qtscriptversion.h

%{_qt5_libdir}/cmake/Qt5Script
%{_qt5_prefix}/mkspecs/modules/qt_lib_script.pri
%{_qt5_exampledir}/script

#------------------------------------------------------------------------------

%package -n	%{qtscript_p_d}
Summary:	Devel files needed to build apps based on QtScript
Group:		Development/KDE and Qt
Requires:	%{qtscriptd} = %version
Provides:	qt5-qtscript-private-devel = %version

%description -n %{qtscript_p_d}
Devel files needed to build apps based on QtScript.

%files -n %{qtscript_p_d}
%dir %{_qt5_includedir}/QtScript/%version
%dir %{_qt5_includedir}/QtScript/%version/QtScript
%dir %{_qt5_includedir}/QtScript/%version/QtScript/private
%{_qt5_includedir}/QtScript/%version/QtScript/private/*.h
%{_qt5_prefix}/mkspecs/modules/qt_lib_script_private.pri


%prep
%autosetup -n %qttarballdir -p1

%build
%qmake_qt5
%make_build
#------------------------------------------------------------------------------

%install
%make_install INSTALL_ROOT=%{buildroot}

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt5_libdir}
for prl_file in libQt5*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd

install -d %{buildroot}/%{_qt5_docdir}

# .la and .a files, die, die, die.
rm -f %{buildroot}%{_qt5_libdir}/lib*.la
rm -f %{buildroot}%{_qt5_libdir}/lib*.a
