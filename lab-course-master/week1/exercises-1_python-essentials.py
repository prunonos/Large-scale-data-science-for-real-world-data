<!DOCTYPE html>
<html class="" lang="en">
<head prefix="og: http://ogp.me/ns#">
<meta charset="utf-8">
<link rel="preload" href="/gitlab/assets/application_utilities-890a8bbe18ecbfbbbd26c364e8d31a547e12fe896fdc2c6c000a55eb1ce7cf45.css" as="style" type="text/css">
<link rel="preload" href="/gitlab/assets/application-775f130d36e9eb14cb67c6a63551511b87f78944cebcf6cdddb78292030341df.css" as="style" type="text/css">
<link rel="preload" href="/gitlab/assets/highlight/themes/white-88d7a77ed7cff657c57dd5a7ae597ced9b0e66e902df5e026af3f8b786c26fec.css" as="style" type="text/css">

<meta content="IE=edge" http-equiv="X-UA-Compatible">
<script>
//<![CDATA[
var gl = window.gl || {};
gl.startup_calls = {"/gitlab/prunonos/com490-lab-course/-/blob/master/week1/exercises-1_python-essentials.py?format=json\u0026viewer=simple":{}};
gl.startup_graphql_calls = null;

if (gl.startup_calls && window.fetch) {
  Object.keys(gl.startup_calls).forEach(apiCall => {
   gl.startup_calls[apiCall] = {
      fetchCall: fetch(apiCall, {
        // Emulate XHR for Rails AJAX request checks
        headers: {
          'X-Requested-With': 'XMLHttpRequest'
        },
        // fetch won’t send cookies in older browsers, unless you set the credentials init option.
        // We set to `same-origin` which is default value in modern browsers.
        // See https://github.com/whatwg/fetch/pull/585 for more information.
        credentials: 'same-origin'
      })
    };
  });
}
if (gl.startup_graphql_calls && window.fetch) {
  const headers = {"X-CSRF-Token":"/NDzS/EL++8yctHxrSIRYhwVeQF9a0u1xbDj0qQWdRwxm2lL+mZP59a1u81mco61Ftra5BAxLW6daUQ4yNrsMw==","x-gitlab-feature-category":"source_code_management"};
  const url = `https://dslab2022-renku.epfl.ch/gitlab/api/graphql`

  const opts = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...headers,
    }
  };

  gl.startup_graphql_calls = gl.startup_graphql_calls.map(call => ({
    ...call,
    fetchCall: fetch(url, {
      ...opts,
      credentials: 'same-origin',
      body: JSON.stringify(call)
    })
  }))
}


//]]>
</script>
<meta content="object" property="og:type">
<meta content="GitLab" property="og:site_name">
<meta content="week1/exercises-1_python-essentials.py · master · Guillem Pruñonosa Soler / com490-lab-course" property="og:title">
<meta content="GitLab Community Edition" property="og:description">
<meta content="https://dslab2022-renku.epfl.ch/gitlab/assets/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png" property="og:image">
<meta content="64" property="og:image:width">
<meta content="64" property="og:image:height">
<meta content="https://dslab2022-renku.epfl.ch/gitlab/prunonos/com490-lab-course/-/blob/master/week1/exercises-1_python-essentials.py" property="og:url">
<meta content="summary" property="twitter:card">
<meta content="week1/exercises-1_python-essentials.py · master · Guillem Pruñonosa Soler / com490-lab-course" property="twitter:title">
<meta content="GitLab Community Edition" property="twitter:description">
<meta content="https://dslab2022-renku.epfl.ch/gitlab/assets/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png" property="twitter:image">

<title>week1/exercises-1_python-essentials.py · master · Guillem Pruñonosa Soler / com490-lab-course · GitLab</title>
<meta content="GitLab Community Edition" name="description">
<link rel="prefetch" href="/gitlab/assets/webpack/monaco.6706c0e6.chunk.js">
<link rel="shortcut icon" type="image/png" href="/gitlab/assets/favicon-7901bd695fb93edb07975966062049829afb56cf11511236e61bcf425070e36e.png" id="favicon" data-original-href="/gitlab/assets/favicon-7901bd695fb93edb07975966062049829afb56cf11511236e61bcf425070e36e.png" />
<style>
@keyframes blinking-dot{0%{opacity:1}25%{opacity:0.4}75%{opacity:0.4}100%{opacity:1}}@keyframes blinking-scroll-button{0%{opacity:0.2}50%{opacity:1}100%{opacity:0.2}}@keyframes gl-spinner-rotate{0%{transform:rotate(0)}100%{transform:rotate(360deg)}}body.ui-indigo .navbar-gitlab{background-color:#292961}body.ui-indigo .navbar-gitlab .navbar-collapse{color:#d1d1f0}body.ui-indigo .navbar-gitlab .container-fluid .navbar-toggler{border-left:1px solid #6868b9;color:#d1d1f0}body.ui-indigo .navbar-gitlab .navbar-sub-nav>li>a:hover,body.ui-indigo .navbar-gitlab .navbar-sub-nav>li>a:focus,body.ui-indigo .navbar-gitlab .navbar-sub-nav>li>button:hover,body.ui-indigo .navbar-gitlab .navbar-sub-nav>li>button:focus,body.ui-indigo .navbar-gitlab .navbar-nav>li>a:hover,body.ui-indigo .navbar-gitlab .navbar-nav>li>a:focus,body.ui-indigo .navbar-gitlab .navbar-nav>li>button:hover,body.ui-indigo .navbar-gitlab .navbar-nav>li>button:focus{background-color:rgba(209,209,240,0.2)}body.ui-indigo .navbar-gitlab .navbar-sub-nav>li.active>a,body.ui-indigo .navbar-gitlab .navbar-sub-nav>li.active>button,body.ui-indigo .navbar-gitlab .navbar-sub-nav>li.dropdown.show>a,body.ui-indigo .navbar-gitlab .navbar-sub-nav>li.dropdown.show>button,body.ui-indigo .navbar-gitlab .navbar-nav>li.active>a,body.ui-indigo .navbar-gitlab .navbar-nav>li.active>button,body.ui-indigo .navbar-gitlab .navbar-nav>li.dropdown.show>a,body.ui-indigo .navbar-gitlab .navbar-nav>li.dropdown.show>button{color:#292961;background-color:#fff}body.ui-indigo .navbar-gitlab .navbar-sub-nav>li.line-separator,body.ui-indigo .navbar-gitlab .navbar-nav>li.line-separator{border-left:1px solid rgba(209,209,240,0.2)}body.ui-indigo .navbar-gitlab .navbar-sub-nav{color:#d1d1f0}body.ui-indigo .navbar-gitlab .nav>li{color:#d1d1f0}body.ui-indigo .navbar-gitlab .nav>li>a .notification-dot{border:2px solid #292961}body.ui-indigo .navbar-gitlab .nav>li>a.header-help-dropdown-toggle .notification-dot{background-color:#d1d1f0}body.ui-indigo .navbar-gitlab .nav>li>a.header-user-dropdown-toggle .header-user-avatar{border-color:#d1d1f0}@media (min-width: 576px){body.ui-indigo .navbar-gitlab .nav>li>a:hover,body.ui-indigo .navbar-gitlab .nav>li>a:focus{background-color:rgba(209,209,240,0.2)}}body.ui-indigo .navbar-gitlab .nav>li>a:hover svg,body.ui-indigo .navbar-gitlab .nav>li>a:focus svg{fill:currentColor}body.ui-indigo .navbar-gitlab .nav>li>a:hover .notification-dot,body.ui-indigo .navbar-gitlab .nav>li>a:focus .notification-dot{will-change:border-color, background-color;border-color:#4a4a82}body.ui-indigo .navbar-gitlab .nav>li>a:hover.header-help-dropdown-toggle .notification-dot,body.ui-indigo .navbar-gitlab .nav>li>a:focus.header-help-dropdown-toggle .notification-dot{background-color:#fff}body.ui-indigo .navbar-gitlab .nav>li.active>a,body.ui-indigo .navbar-gitlab .nav>li.dropdown.show>a{color:#292961;background-color:#fff}body.ui-indigo .navbar-gitlab .nav>li.active>a:hover svg,body.ui-indigo .navbar-gitlab .nav>li.dropdown.show>a:hover svg{fill:#292961}body.ui-indigo .navbar-gitlab .nav>li.active>a .notification-dot,body.ui-indigo .navbar-gitlab .nav>li.dropdown.show>a .notification-dot{border-color:#fff}body.ui-indigo .navbar-gitlab .nav>li.active>a.header-help-dropdown-toggle .notification-dot,body.ui-indigo .navbar-gitlab .nav>li.dropdown.show>a.header-help-dropdown-toggle .notification-dot{background-color:#292961}body.ui-indigo .navbar-gitlab .nav>li .impersonated-user svg,body.ui-indigo .navbar-gitlab .nav>li .impersonated-user:hover svg{fill:#292961}body.ui-indigo .navbar .title>a:hover,body.ui-indigo .navbar .title>a:focus{background-color:rgba(209,209,240,0.2)}body.ui-indigo .header-search{background-color:rgba(209,209,240,0.2) !important}body.ui-indigo .header-search:hover{background-color:rgba(209,209,240,0.3) !important}body.ui-indigo .header-search svg{color:rgba(209,209,240,0.8) !important}body.ui-indigo .header-search input{background-color:transparent;color:rgba(209,209,240,0.8)}body.ui-indigo .header-search input::placeholder{color:rgba(209,209,240,0.8)}body.ui-indigo .header-search input:focus::placeholder,body.ui-indigo .header-search input:active::placeholder{color:#d1d1f0}body.ui-indigo .search form{background-color:rgba(209,209,240,0.2)}body.ui-indigo .search form:hover{background-color:rgba(209,209,240,0.3)}body.ui-indigo .search .search-input::placeholder{color:rgba(209,209,240,0.8)}body.ui-indigo .search .search-input-wrap .search-icon,body.ui-indigo .search .search-input-wrap .clear-icon{fill:rgba(209,209,240,0.8)}body.ui-indigo .search.search-active form{background-color:#fff}body.ui-indigo .search.search-active .search-input-wrap .search-icon{fill:rgba(209,209,240,0.8)}body.ui-indigo .nav-sidebar li.active>a{color:#2f2a6b}body.ui-indigo .nav-sidebar .fly-out-top-item a,body.ui-indigo .nav-sidebar .fly-out-top-item a:hover,body.ui-indigo .nav-sidebar .fly-out-top-item.active a,body.ui-indigo .nav-sidebar .fly-out-top-item .fly-out-top-item-container{background-color:var(--gray-100, #f0f0f0);color:var(--gray-900, #303030)}body.ui-indigo .nav-links li.active a,body.ui-indigo .nav-links li.md-header-tab.active button,body.ui-indigo .nav-links li a.active{border-bottom:2px solid #6666c4}body.ui-indigo .nav-links li.active a .badge.badge-pill,body.ui-indigo .nav-links li.md-header-tab.active button .badge.badge-pill,body.ui-indigo .nav-links li a.active .badge.badge-pill{font-weight:600}body.ui-indigo .emoji-picker-category-active{border-bottom-color:#6666c4}body.ui-indigo .branch-header-title{color:#4b4ba3}body.ui-indigo .ide-sidebar-link.active{color:#4b4ba3}body.ui-indigo .ide-sidebar-link.active.is-right{box-shadow:inset -3px 0 #4b4ba3}

*,*::before,*::after{box-sizing:border-box}html{font-family:sans-serif;line-height:1.15}aside,header{display:block}body{margin:0;font-family:-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans", Ubuntu, Cantarell, "Helvetica Neue", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";font-size:1rem;font-weight:400;line-height:1.5;color:#303030;text-align:left;background-color:#fff}h1{margin-top:0;margin-bottom:0.25rem}ul{margin-top:0;margin-bottom:1rem}ul ul{margin-bottom:0}strong{font-weight:bolder}a{color:#007bff;text-decoration:none;background-color:transparent}a:not([href]):not([class]){color:inherit;text-decoration:none}img{vertical-align:middle;border-style:none}svg{overflow:hidden;vertical-align:middle}button{border-radius:0}input,button{margin:0;font-family:inherit;font-size:inherit;line-height:inherit}button,input{overflow:visible}button{text-transform:none}[role="button"]{cursor:pointer}button:not(:disabled),[type="button"]:not(:disabled){cursor:pointer}button::-moz-focus-inner,[type="button"]::-moz-focus-inner{padding:0;border-style:none}[type="search"]{outline-offset:-2px}h1{margin-bottom:0.25rem;font-weight:600;line-height:1.2;color:#303030}h1{font-size:2.1875rem}.list-unstyled{padding-left:0;list-style:none}.container-fluid{width:100%;padding-right:15px;padding-left:15px;margin-right:auto;margin-left:auto}.form-control{display:block;width:100%;height:34px;padding:0.375rem 0.75rem;font-size:0.875rem;font-weight:400;line-height:1.5;color:#303030;background-color:#fff;background-clip:padding-box;border:1px solid #dbdbdb;border-radius:0.25rem}.form-control:-moz-focusring{color:transparent;text-shadow:0 0 0 #303030}.form-control::placeholder{color:#5e5e5e;opacity:1}.form-control:disabled{background-color:#fafafa;opacity:1}.form-inline{display:flex;flex-flow:row wrap;align-items:center}@media (min-width: 576px){.form-inline .form-control{display:inline-block;width:auto;vertical-align:middle}}.btn{display:inline-block;font-weight:400;color:#303030;text-align:center;vertical-align:middle;-webkit-user-select:none;user-select:none;background-color:transparent;border:1px solid transparent;padding:0.375rem 0.75rem;font-size:1rem;line-height:20px;border-radius:0.25rem}.btn:disabled{opacity:0.65}.btn:not(:disabled):not(.disabled){cursor:pointer}.collapse:not(.show){display:none}.dropdown{position:relative}.dropdown-menu{position:absolute;top:100%;left:0;z-index:1000;display:none;float:left;min-width:10rem;padding:0.5rem 0;margin:0.125rem 0 0;font-size:1rem;color:#303030;text-align:left;list-style:none;background-color:#fff;background-clip:padding-box;border:1px solid rgba(0,0,0,0.15);border-radius:0.25rem}.nav{display:flex;flex-wrap:wrap;padding-left:0;margin-bottom:0;list-style:none}.navbar{position:relative;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;padding:0.25rem 0.5rem}.navbar .container-fluid{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between}.navbar-nav{display:flex;flex-direction:column;padding-left:0;margin-bottom:0;list-style:none}.navbar-nav .dropdown-menu{position:static;float:none}.navbar-collapse{flex-basis:100%;flex-grow:1;align-items:center}.navbar-toggler{padding:0.25rem 0.75rem;font-size:1.25rem;line-height:1;background-color:transparent;border:1px solid transparent;border-radius:0.25rem}@media (max-width: 575.98px){.navbar-expand-sm>.container-fluid{padding-right:0;padding-left:0}}@media (min-width: 576px){.navbar-expand-sm{flex-flow:row nowrap;justify-content:flex-start}.navbar-expand-sm .navbar-nav{flex-direction:row}.navbar-expand-sm .navbar-nav .dropdown-menu{position:absolute}.navbar-expand-sm>.container-fluid{flex-wrap:nowrap}.navbar-expand-sm .navbar-collapse{display:flex !important;flex-basis:auto}.navbar-expand-sm .navbar-toggler{display:none}}.badge{display:inline-block;padding:0.25em 0.4em;font-size:75%;font-weight:600;line-height:1;text-align:center;white-space:nowrap;vertical-align:baseline;border-radius:0.25rem}.badge:empty{display:none}.btn .badge{position:relative;top:-1px}.badge-pill{padding-right:0.6em;padding-left:0.6em;border-radius:10rem}.bg-transparent{background-color:transparent !important}.rounded-circle{border-radius:50% !important}.d-none{display:none !important}.d-block{display:block !important}@media (min-width: 576px){.d-sm-none{display:none !important}.d-sm-inline-block{display:inline-block !important}}@media (min-width: 768px){.d-md-block{display:block !important}}@media (min-width: 992px){.d-lg-none{display:none !important}.d-lg-block{display:block !important}}.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0, 0, 0, 0);white-space:nowrap;border:0}.m-auto{margin:auto !important}.gl-badge{display:inline-flex;align-items:center;font-size:0.75rem;font-weight:400;line-height:1rem;padding-top:0.25rem;padding-bottom:0.25rem;padding-left:0.5rem;padding-right:0.5rem}.gl-button .gl-badge{top:0}.gl-form-input,.gl-form-input.form-control{background-color:#fff;font-family:-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans", Ubuntu, Cantarell, "Helvetica Neue", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";font-size:0.875rem;line-height:1rem;padding-top:0.5rem;padding-bottom:0.5rem;padding-left:0.75rem;padding-right:0.75rem;height:auto;color:#303030;box-shadow:inset 0 0 0 1px #868686;border-style:none;-webkit-appearance:none;appearance:none;-moz-appearance:none}.gl-form-input:disabled,.gl-form-input:not(.form-control-plaintext):not([type="color"]):read-only,.gl-form-input.form-control:disabled,.gl-form-input.form-control:not(.form-control-plaintext):not([type="color"]):read-only{background-color:#fafafa;color:#868686;box-shadow:inset 0 0 0 1px #dbdbdb;cursor:not-allowed}.gl-form-input::placeholder,.gl-form-input.form-control::placeholder{color:#868686}.gl-button{display:inline-flex}.gl-button:not(.btn-link):active{text-decoration:none}.gl-button.gl-button{border-width:0;padding-top:0.5rem;padding-bottom:0.5rem;padding-left:0.75rem;padding-right:0.75rem;background-color:transparent;line-height:1rem;color:#303030;fill:currentColor;box-shadow:inset 0 0 0 1px #bfbfbf;justify-content:center;align-items:center;font-size:0.875rem;border-radius:0.25rem}.gl-button.gl-button.btn-default{background-color:#fff}.gl-button.gl-button.btn-default:active,.gl-button.gl-button.btn-default.active{box-shadow:inset 0 0 0 2px #5e5e5e,0 0 0 1px rgba(255,255,255,0.4),0 0 0 4px rgba(31,117,203,0.48);outline:none;background-color:#dbdbdb}body,.form-control,.search form{font-size:0.875rem}button,html [type="button"],[role="button"]{cursor:pointer}h1{margin-top:20px;margin-bottom:10px}strong{font-weight:bold}a{color:#1068bf}.hidden{display:none !important;visibility:hidden !important}.hide{display:none}.badge:not(.gl-badge){padding:4px 5px;font-size:12px;font-style:normal;font-weight:400;display:inline-block}.divider{height:0;margin:4px 0;overflow:hidden;border-top:1px solid #dbdbdb}.toggle-sidebar-button .collapse-text,.toggle-sidebar-button .icon-chevron-double-lg-left{color:#666}svg{vertical-align:baseline}html{overflow-y:scroll}body{text-decoration-skip:ink}.btn{border-radius:4px;font-size:0.875rem;font-weight:400;padding:6px 10px;background-color:#fff;border-color:#dbdbdb;color:#303030;color:#303030;white-space:nowrap}.btn:active{background-color:#f0f0f0;box-shadow:none}.btn:active,.btn.active{background-color:#eaeaea;border-color:#e3e3e3;color:#303030}.btn svg{height:15px;width:15px}.btn svg:not(:last-child){margin-right:5px}.badge.badge-pill:not(.gl-badge){font-weight:400;background-color:rgba(0,0,0,0.07);color:#525252;vertical-align:baseline}.gl-font-sm{font-size:12px}.dropdown{position:relative}.search-input-container .dropdown-menu{margin-top:11px}.dropdown-menu-toggle{padding:6px 8px 6px 10px;background-color:#fff;color:#303030;font-size:14px;text-align:left;border:1px solid #dbdbdb;border-radius:0.25rem;white-space:nowrap}.dropdown-menu-toggle.no-outline{outline:0}.dropdown-menu-toggle.dropdown-menu-toggle{justify-content:flex-start;overflow:hidden;padding-right:25px;position:relative;text-overflow:ellipsis;width:160px}.dropdown-menu{display:none;position:absolute;width:auto;top:100%;z-index:300;min-width:240px;max-width:500px;margin-top:4px;margin-bottom:24px;font-size:0.875rem;font-weight:400;padding:8px 0;background-color:#fff;border:1px solid #dbdbdb;border-radius:0.25rem;box-shadow:0 2px 4px rgba(0,0,0,0.1)}.dropdown-menu ul{margin:0;padding:0}.dropdown-menu li{display:block;text-align:left;list-style:none;padding:0 1px}.dropdown-menu li>a,.dropdown-menu li button{background:transparent;border:0;border-radius:0;box-shadow:none;display:block;font-weight:400;position:relative;padding:8px 12px;color:#303030;line-height:16px;white-space:normal;overflow:hidden;text-align:left;width:100%}.dropdown-menu li>a:active,.dropdown-menu li button:active{background-color:#eee;color:#303030;outline:0;text-decoration:none}.dropdown-menu .divider{height:1px;margin:0.25rem 0;padding:0;background-color:#dbdbdb}.dropdown-menu .badge.badge-pill+span:not(.badge):not(.badge-pill){margin-right:40px}@media (max-width: 575.98px){.navbar-gitlab li.dropdown{position:static}.navbar-gitlab li.dropdown.user-counter{margin-left:8px !important}.navbar-gitlab li.dropdown.user-counter>a{padding:0 4px !important}header.navbar-gitlab .dropdown .dropdown-menu{width:100%;min-width:100%}}@media (max-width: 767.98px){.dropdown-menu-toggle{width:100%}}input{border-radius:0.25rem;color:#303030;background-color:#fff}.form-control{border-radius:4px;padding:6px 10px}.form-control::placeholder{color:#868686}.navbar-gitlab{padding:0 16px;z-index:1000;margin-bottom:0;min-height:40px;border:0;position:fixed;top:0;left:0;right:0;border-radius:0}.navbar-gitlab .logo-text{line-height:initial}.navbar-gitlab .logo-text svg{width:55px;height:14px;margin:0;fill:#fff}.navbar-gitlab .close-icon{display:none}.navbar-gitlab .header-content{width:100%;display:flex;justify-content:space-between;position:relative;min-height:40px;padding-left:0}.navbar-gitlab .header-content .title-container{display:flex;align-items:stretch;flex:1 1 auto;padding-top:0;overflow:visible}.navbar-gitlab .header-content .title{padding-right:0;color:currentColor;display:flex;position:relative;margin:0;font-size:18px;vertical-align:top;white-space:nowrap}.navbar-gitlab .header-content .title img{height:28px}.navbar-gitlab .header-content .title img+.logo-text{margin-left:8px}.navbar-gitlab .header-content .title a{display:flex;align-items:center;padding:2px 8px;margin:5px 2px 5px -8px;border-radius:4px}.navbar-gitlab .header-content .navbar-collapse>ul.nav>li:not(.d-none){margin:0 2px}.navbar-gitlab .navbar-collapse{flex:0 0 auto;border-top:0;padding:0}@media (max-width: 575.98px){.navbar-gitlab .navbar-collapse{flex:1 1 auto}}.navbar-gitlab .navbar-collapse .nav{flex-wrap:nowrap}@media (max-width: 575.98px){.navbar-gitlab .navbar-collapse .nav>li:not(.d-none) a{margin-left:0}}.navbar-gitlab .container-fluid{padding:0}.navbar-gitlab .container-fluid .user-counter svg{margin-right:3px}.navbar-gitlab .container-fluid .navbar-toggler{position:relative;right:-10px;border-radius:0;min-width:45px;padding:0;margin:8px -7px 8px 0;font-size:14px;text-align:center;color:currentColor}.navbar-gitlab .container-fluid .navbar-toggler.active{color:currentColor;background-color:transparent}@media (max-width: 575.98px){.navbar-gitlab .container-fluid .navbar-nav{display:flex;padding-right:10px;flex-direction:row}}.navbar-gitlab .container-fluid .navbar-nav li .badge.badge-pill:not(.merge-request-badge){box-shadow:none;font-weight:600}@media (max-width: 575.98px){.navbar-gitlab .container-fluid .nav>li.header-user{padding-left:10px}}.navbar-gitlab .container-fluid .nav>li>a{will-change:color;margin:4px 0;padding:6px 8px;height:32px}@media (max-width: 575.98px){.navbar-gitlab .container-fluid .nav>li>a{padding:0}}.navbar-gitlab .container-fluid .nav>li>a.header-user-dropdown-toggle{margin-left:2px}.navbar-gitlab .container-fluid .nav>li>a.header-user-dropdown-toggle .header-user-avatar{margin-right:0}.navbar-gitlab .container-fluid .nav>li .header-new-dropdown-toggle{margin-right:0}.navbar-sub-nav>li>a,.navbar-sub-nav>li>button,.navbar-nav>li>a,.navbar-nav>li>button{display:flex;align-items:center;justify-content:center;padding:6px 8px;margin:4px 2px;font-size:12px;color:currentColor;border-radius:4px;height:32px;font-weight:600}.navbar-sub-nav>li .top-nav-toggle,.navbar-sub-nav>li>button,.navbar-nav>li .top-nav-toggle,.navbar-nav>li>button{background:transparent;border:0}.navbar-sub-nav .dropdown-menu,.navbar-nav .dropdown-menu{position:absolute}.navbar-sub-nav{display:flex;margin:0 0 0 6px}.caret-down,.btn .caret-down{top:0;height:11px;width:11px;margin-left:4px;fill:currentColor}.header-user .dropdown-menu,.header-new .dropdown-menu{margin-top:4px}.btn-sign-in{background-color:#ebebfa;color:#292961;font-weight:600;line-height:18px;margin:4px 0 4px 2px}.title-container .badge.badge-pill:not(.merge-request-badge),.navbar-nav .badge.badge-pill:not(.merge-request-badge){position:inherit;font-weight:400;margin-left:-6px;font-size:11px;color:var(--gray-950, #fff);padding:0 5px;line-height:12px;border-radius:7px;box-shadow:0 1px 0 rgba(76,78,84,0.2)}.title-container .badge.badge-pill:not(.merge-request-badge).green-badge,.navbar-nav .badge.badge-pill:not(.merge-request-badge).green-badge{background-color:var(--green-400, #2da160)}.title-container .badge.badge-pill:not(.merge-request-badge).merge-requests-count,.navbar-nav .badge.badge-pill:not(.merge-request-badge).merge-requests-count{background-color:var(--orange-400, #c17d10)}.title-container .badge.badge-pill:not(.merge-request-badge).todos-count,.navbar-nav .badge.badge-pill:not(.merge-request-badge).todos-count{background-color:var(--blue-400, #428fdc)}.title-container .canary-badge .badge,.navbar-nav .canary-badge .badge{font-size:12px;line-height:16px;padding:0 0.5rem}@media (max-width: 575.98px){.navbar-gitlab .container-fluid{font-size:18px}.navbar-gitlab .container-fluid .navbar-nav{table-layout:fixed;width:100%;margin:0;text-align:right}.navbar-gitlab .container-fluid .navbar-collapse{margin-left:-8px;margin-right:-10px}.navbar-gitlab .container-fluid .navbar-collapse .nav>li:not(.d-none){flex:1}.header-user-dropdown-toggle{text-align:center}.header-user-avatar{float:none}}.header-user-avatar{float:left;margin-right:5px;border-radius:50%;border:1px solid #f5f5f5}.notification-dot{background-color:#d99530;height:12px;width:12px;margin-top:-15px;pointer-events:none;visibility:hidden}.top-nav-toggle .dropdown-icon{margin-right:0.5rem}.tanuki-logo .tanuki-left-ear,.tanuki-logo .tanuki-right-ear,.tanuki-logo .tanuki-nose{fill:#e24329}.tanuki-logo .tanuki-left-eye,.tanuki-logo .tanuki-right-eye{fill:#fc6d26}.tanuki-logo .tanuki-left-cheek,.tanuki-logo .tanuki-right-cheek{fill:#fca326}.context-header{position:relative;margin-right:2px;width:220px}.context-header>a,.context-header>button{font-weight:600;display:flex;width:100%;align-items:center;padding:10px 16px 10px 10px;color:#303030;background-color:transparent;border:0;text-align:left}.context-header .avatar-container{flex:0 0 40px;background-color:#fff}.context-header .sidebar-context-title{overflow:hidden;text-overflow:ellipsis;color:#303030}@media (min-width: 768px){.page-with-contextual-sidebar{padding-left:48px}}@media (min-width: 1200px){.page-with-contextual-sidebar{padding-left:220px}}@media (min-width: 768px){.page-with-icon-sidebar{padding-left:48px}}.nav-sidebar{position:fixed;bottom:0;left:0;z-index:600;width:220px;top:40px;background-color:#f0f0f0;transform:translate3d(0, 0, 0)}.nav-sidebar.sidebar-collapsed-desktop{width:48px}.nav-sidebar.sidebar-collapsed-desktop .nav-sidebar-inner-scroll{overflow-x:hidden}.nav-sidebar.sidebar-collapsed-desktop .badge.badge-pill:not(.fly-out-badge),.nav-sidebar.sidebar-collapsed-desktop .nav-item-name,.nav-sidebar.sidebar-collapsed-desktop .collapse-text{border:0;clip:rect(0, 0, 0, 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;white-space:nowrap;width:1px}.nav-sidebar.sidebar-collapsed-desktop .sidebar-top-level-items>li>a{min-height:unset}.nav-sidebar.sidebar-collapsed-desktop .fly-out-top-item:not(.divider){display:block !important}.nav-sidebar.sidebar-collapsed-desktop .avatar-container{margin:0 auto}.nav-sidebar.sidebar-collapsed-desktop li.active:not(.fly-out-top-item)>a{background-color:rgba(41,41,97,0.08)}.nav-sidebar a{text-decoration:none;color:#303030}.nav-sidebar li{white-space:nowrap}.nav-sidebar li .nav-item-name{flex:1}.nav-sidebar li>a,.nav-sidebar li>.fly-out-top-item-container{padding-left:0.75rem;padding-right:0.75rem;padding-top:0.5rem;padding-bottom:0.5rem;display:flex;align-items:center;border-radius:0.25rem;width:auto;line-height:1rem;margin:1px 4px}.nav-sidebar li.active>a{font-weight:600}.nav-sidebar li.active:not(.fly-out-top-item)>a:not(.has-sub-items){background-color:rgba(41,41,97,0.08)}.nav-sidebar ul{padding-left:0;list-style:none}@media (max-width: 767.98px){.nav-sidebar{left:-220px}}.nav-sidebar .nav-icon-container{display:flex;margin-right:8px}.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item{display:none}.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item a,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item.active a,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item .fly-out-top-item-container{margin-left:0;margin-right:0;padding-left:1rem;padding-right:1rem;cursor:default;pointer-events:none;font-size:0.75rem;margin-top:-0.25rem;margin-bottom:-0.25rem;margin-top:0;position:relative;color:#fff;background:var(--black, #000)}.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item a strong,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item.active a strong,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item .fly-out-top-item-container strong{font-weight:400}.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item a::before,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item.active a::before,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item .fly-out-top-item-container::before{position:absolute;content:"";display:block;top:50%;left:-0.25rem;margin-top:-0.25rem;width:0;height:0;border-top:0.25rem solid transparent;border-bottom:0.25rem solid transparent;border-right:0.25rem solid #000;border-right-color:var(--black, #000)}.nav-sidebar a.has-sub-items+.sidebar-sub-level-items .fly-out-top-item{display:none}.nav-sidebar a.has-sub-items+.sidebar-sub-level-items .fly-out-top-item a,.nav-sidebar a.has-sub-items+.sidebar-sub-level-items .fly-out-top-item.active a,.nav-sidebar a.has-sub-items+.sidebar-sub-level-items .fly-out-top-item .fly-out-top-item-container{margin-left:0;margin-right:0;padding-left:1rem;padding-right:1rem;cursor:default;pointer-events:none;font-size:0.75rem;margin-top:0;border-bottom-left-radius:0;border-bottom-right-radius:0}@media (min-width: 768px) and (max-width: 1199px){.nav-sidebar:not(.sidebar-expanded-mobile){width:48px}.nav-sidebar:not(.sidebar-expanded-mobile) .nav-sidebar-inner-scroll{overflow-x:hidden}.nav-sidebar:not(.sidebar-expanded-mobile) .badge.badge-pill:not(.fly-out-badge),.nav-sidebar:not(.sidebar-expanded-mobile) .nav-item-name,.nav-sidebar:not(.sidebar-expanded-mobile) .collapse-text{border:0;clip:rect(0, 0, 0, 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;white-space:nowrap;width:1px}.nav-sidebar:not(.sidebar-expanded-mobile) .sidebar-top-level-items>li>a{min-height:unset}.nav-sidebar:not(.sidebar-expanded-mobile) .fly-out-top-item:not(.divider){display:block !important}.nav-sidebar:not(.sidebar-expanded-mobile) .avatar-container{margin:0 auto}.nav-sidebar:not(.sidebar-expanded-mobile) li.active:not(.fly-out-top-item)>a{background-color:rgba(41,41,97,0.08)}.nav-sidebar:not(.sidebar-expanded-mobile) .context-header{height:60px;width:48px}.nav-sidebar:not(.sidebar-expanded-mobile) .context-header a{padding:10px 4px}.nav-sidebar:not(.sidebar-expanded-mobile) .sidebar-context-title{border:0;clip:rect(0, 0, 0, 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;white-space:nowrap;width:1px}.nav-sidebar:not(.sidebar-expanded-mobile) .context-header{height:auto}.nav-sidebar:not(.sidebar-expanded-mobile) .context-header a{padding:0.25rem}.nav-sidebar:not(.sidebar-expanded-mobile) .sidebar-top-level-items>li .sidebar-sub-level-items:not(.flyout-list){display:none}.nav-sidebar:not(.sidebar-expanded-mobile) .nav-icon-container{margin-right:0}.nav-sidebar:not(.sidebar-expanded-mobile) .toggle-sidebar-button{width:48px}.nav-sidebar:not(.sidebar-expanded-mobile) .toggle-sidebar-button .collapse-text{display:none}.nav-sidebar:not(.sidebar-expanded-mobile) .toggle-sidebar-button .icon-chevron-double-lg-left{transform:rotate(180deg);margin:0}}.nav-sidebar-inner-scroll{height:100%;width:100%;overflow:auto}.nav-sidebar-inner-scroll>div.context-header{margin-top:0.25rem}.nav-sidebar-inner-scroll>div.context-header a{padding-left:0.75rem;padding-right:0.75rem;padding-top:0.5rem;padding-bottom:0.5rem;display:flex;align-items:center;border-radius:0.25rem;width:auto;line-height:1rem;margin:1px 4px;padding:0.25rem;margin-bottom:0.25rem;margin-top:0}.nav-sidebar-inner-scroll>div.context-header a .avatar-container{font-weight:400;flex:none;box-shadow:inset 0 0 0 1px rgba(0,0,0,0.08)}.nav-sidebar-inner-scroll>div.context-header a .avatar-container.rect-avatar{border-style:none}.nav-sidebar-inner-scroll>div.context-header a .avatar-container.rect-avatar .avatar.s32{border-radius:4px;box-shadow:inset 0 0 0 1px rgba(0,0,0,0.08)}.sidebar-top-level-items{margin-top:0.25rem;margin-bottom:60px}.sidebar-top-level-items .context-header a{padding:0.25rem;margin-bottom:0.25rem;margin-top:0}.sidebar-top-level-items .context-header a .avatar-container{font-weight:400;flex:none;box-shadow:inset 0 0 0 1px rgba(0,0,0,0.08)}.sidebar-top-level-items .context-header a .avatar-container.rect-avatar{border-style:none}.sidebar-top-level-items .context-header a .avatar-container.rect-avatar .avatar.s32{border-radius:4px;box-shadow:inset 0 0 0 1px rgba(0,0,0,0.08)}.sidebar-top-level-items>li .badge.badge-pill{border-radius:0.5rem;padding-top:0.125rem;padding-bottom:0.125rem;padding-left:0.5rem;padding-right:0.5rem;background-color:#cbe2f9;color:#0b5cad}.sidebar-top-level-items>li.active .sidebar-sub-level-items:not(.is-fly-out-only){display:block}.sidebar-top-level-items>li.active .badge.badge-pill{font-weight:400;color:#0b5cad}.sidebar-sub-level-items{padding-top:0;padding-bottom:0;display:none}.sidebar-sub-level-items:not(.fly-out-list) li>a{padding-left:2.25rem}.toggle-sidebar-button,.close-nav-button{height:48px;padding:0 16px;background-color:#fafafa;border:0;color:#666;display:flex;align-items:center;background-color:#f0f0f0;border-top:1px solid #dbdbdb;position:fixed;bottom:0;width:220px}.toggle-sidebar-button .collapse-text,.toggle-sidebar-button .icon-chevron-double-lg-left,.close-nav-button .collapse-text,.close-nav-button .icon-chevron-double-lg-left{color:inherit}.collapse-text{white-space:nowrap;overflow:hidden}.sidebar-collapsed-desktop .context-header{height:60px;width:48px}.sidebar-collapsed-desktop .context-header a{padding:10px 4px}.sidebar-collapsed-desktop .sidebar-context-title{border:0;clip:rect(0, 0, 0, 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;white-space:nowrap;width:1px}.sidebar-collapsed-desktop .context-header{height:auto}.sidebar-collapsed-desktop .context-header a{padding:0.25rem}.sidebar-collapsed-desktop .sidebar-top-level-items>li .sidebar-sub-level-items:not(.flyout-list){display:none}.sidebar-collapsed-desktop .nav-icon-container{margin-right:0}.sidebar-collapsed-desktop .toggle-sidebar-button{width:48px}.sidebar-collapsed-desktop .toggle-sidebar-button .collapse-text{display:none}.sidebar-collapsed-desktop .toggle-sidebar-button .icon-chevron-double-lg-left{transform:rotate(180deg);margin:0}.close-nav-button{display:none}@media (max-width: 767.98px){.close-nav-button{display:flex}.toggle-sidebar-button{display:none}}input::-moz-placeholder{color:#868686;opacity:1}input::-ms-input-placeholder{color:#868686}input:-ms-input-placeholder{color:#868686}svg{fill:currentColor}svg.s12{width:12px;height:12px}svg.s16{width:16px;height:16px}svg.s32{width:32px;height:32px}svg.s12{vertical-align:-1px}svg.s16{vertical-align:-3px}.header-search{width:320px}.search{margin:0 8px}.search form{display:block;margin:0;padding:4px;width:200px;line-height:24px;height:32px;border:0;border-radius:4px}@media (min-width: 1200px){.search form{width:320px}}.search .search-input{border:0;font-size:14px;padding:0 20px 0 0;margin-left:5px;line-height:25px;width:98%;color:#fff;background:none}.search .search-input-container{display:flex;position:relative}.search .search-input-wrap{width:100%}.search .search-input-wrap .search-icon,.search .search-input-wrap .clear-icon{position:absolute;right:5px;top:4px}.search .search-input-wrap .search-icon{-webkit-user-select:none;user-select:none}.search .search-input-wrap .clear-icon{display:none}.search .search-input-wrap .dropdown{position:static}.search .search-input-wrap .dropdown-menu{left:-5px;max-height:400px;overflow:auto}@media (min-width: 1200px){.search .search-input-wrap .dropdown-menu{width:320px}}.search .identicon{flex-basis:16px;flex-shrink:0;margin-right:4px}.avatar,.avatar-container{float:left;margin-right:16px;border-radius:50%;border:1px solid rgba(0,0,0,0.08)}.avatar.s16,.avatar-container.s16{width:16px;height:16px;margin-right:8px}.avatar.s32,.avatar-container.s32{width:32px;height:32px;margin-right:8px}.avatar{transition-property:none;width:40px;height:40px;padding:0;background:#fdfdfd;overflow:hidden;border-color:rgba(0,0,0,0.1)}.avatar.avatar-tile{border-radius:0;border:0}.identicon{text-align:center;vertical-align:top;color:#303030;background-color:#f0f0f0}.identicon.s16{font-size:10px;line-height:16px}.identicon.s32{font-size:14px;line-height:32px}.identicon.bg1{background-color:#fcf1ef}.identicon.bg2{background-color:#f4f0ff}.identicon.bg3{background-color:#f1f1ff}.identicon.bg4{background-color:#e9f3fc}.identicon.bg5{background-color:#ecf4ee}.identicon.bg6{background-color:#fdf1dd}.identicon.bg7{background-color:#f0f0f0}.avatar-container{overflow:hidden;display:flex}.avatar-container a{width:100%;height:100%;display:flex;text-decoration:none}.avatar-container .avatar{border-radius:0;border:0;height:auto;width:100%;margin:0;align-self:center}.rect-avatar{border-radius:2px}.rect-avatar.s16{border-radius:2px}.rect-avatar.s32{border-radius:4px}.tab-width-8{-moz-tab-size:8;tab-size:8}.gl-sr-only{border:0;clip:rect(0, 0, 0, 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;white-space:nowrap;width:1px}.gl-bg-green-500{background-color:#108548}.gl-border-none\!{border-style:none !important}.gl-rounded-pill{border-radius:0.75rem}.gl-text-white{color:#fff}.gl-display-none{display:none}@media (min-width: 36rem){.gl-sm-display-block{display:block}}.gl-absolute{position:absolute}.gl-px-3{padding-left:0.5rem;padding-right:0.5rem}.gl-pr-2{padding-right:0.25rem}.gl-py-1{padding-top:0.125rem;padding-bottom:0.125rem}.gl-ml-3{margin-left:0.5rem}.gl-mx-0\!{margin-left:0 !important;margin-right:0 !important}.gl-font-sm{font-size:0.75rem}.gl-font-weight-bold{font-weight:600}.content-wrapper>.alert-wrapper,#content-body,.modal-dialog{display:none}

</style>

<link rel="stylesheet" media="print" href="/gitlab/assets/application-775f130d36e9eb14cb67c6a63551511b87f78944cebcf6cdddb78292030341df.css" />

<link rel="stylesheet" media="print" href="/gitlab/assets/application_utilities-890a8bbe18ecbfbbbd26c364e8d31a547e12fe896fdc2c6c000a55eb1ce7cf45.css" />


<link rel="stylesheet" media="print" href="/gitlab/assets/highlight/themes/white-88d7a77ed7cff657c57dd5a7ae597ced9b0e66e902df5e026af3f8b786c26fec.css" />
<script>
//<![CDATA[
document.querySelectorAll('link[media="print"]').forEach(linkTag => {
  linkTag.setAttribute('data-startupcss', 'loading');
  const startupLinkLoadedEvent = new CustomEvent('CSSStartupLinkLoaded');
  linkTag.addEventListener('load',function(){this.media='all';this.setAttribute('data-startupcss', 'loaded');document.dispatchEvent(startupLinkLoadedEvent);},{once: true});
})

//]]>
</script>

<script>
//<![CDATA[
window.gon={};gon.api_version="v4";gon.default_avatar_url="https://dslab2022-renku.epfl.ch/gitlab/assets/no_avatar-849f9c04a3a0d0cea2424ae97b27447dc64a7dbfae83c036c45b403392f0e8ba.png";gon.max_file_size=10;gon.asset_host=null;gon.webpack_public_path="/gitlab/assets/webpack/";gon.relative_url_root="/gitlab";gon.user_color_scheme="white";gon.markdown_surround_selection=true;gon.recaptcha_api_server_url="https://www.google.com/recaptcha/api.js";gon.recaptcha_sitekey=null;gon.gitlab_url="https://dslab2022-renku.epfl.ch/gitlab";gon.revision="838dea1cf23";gon.feature_category="source_code_management";gon.gitlab_logo="/gitlab/assets/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png";gon.sprite_icons="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg";gon.sprite_file_icons="/gitlab/assets/file_icons-c13caf2f3ca00cc2c02b11d373ac288c200b9b4dcddbb52a5027dc07b3eece19.svg";gon.emoji_sprites_css_path="/gitlab/assets/emoji_sprites-3825d771ad697b27553bcece6c17a12969dd7407cf0fe3897aad012efc0bf827.css";gon.select2_css_path="/gitlab/assets/lazy_bundles/select2-d720397d08b21964ee0c701ea40aa6286d8928eab7edfac24d05b3c63c466b81.css";gon.test_env=false;gon.disable_animations=null;gon.suggested_label_colors={"#009966":"Green-cyan","#8fbc8f":"Dark sea green","#3cb371":"Medium sea green","#00b140":"Green screen","#013220":"Dark green","#6699cc":"Blue-gray","#0000ff":"Blue","#e6e6fa":"Lavendar","#9400d3":"Dark violet","#330066":"Deep violet","#808080":"Gray","#36454f":"Charcoal grey","#f7e7ce":"Champagne","#c21e56":"Rose red","#cc338b":"Magenta-pink","#dc143c":"Crimson","#ff0000":"Red","#cd5b45":"Dark coral","#eee600":"Titanium yellow","#ed9121":"Carrot orange","#c39953":"Aztec Gold"};gon.first_day_of_week=0;gon.time_display_relative=true;gon.ee=false;gon.jh=false;gon.dot_com=false;gon.current_user_id=67;gon.current_username="prunonos";gon.current_user_fullname="Guillem Pruñonosa Soler";gon.current_user_avatar_url="https://secure.gravatar.com/avatar/4c73ce167ffa00867a43a4450e07ceb5?s=80\u0026d=identicon";gon.features={"snippetsBinaryBlob":false,"usageDataApi":true,"securityAutoFix":false,"improvedEmojiPicker":true,"newHeaderSearch":false,"suppressApolloErrorsDuringNavigation":false,"refactorBlobViewer":false,"refactorTextViewer":false,"consolidatedEditButton":false};
//]]>
</script>




<script src="/gitlab/assets/webpack/runtime.3da5754e.bundle.js" defer="defer"></script>
<script src="/gitlab/assets/webpack/main.d8f1c476.chunk.js" defer="defer"></script>
<script src="/gitlab/assets/webpack/graphql.f82a5a48.chunk.js" defer="defer"></script>
<script src="/gitlab/assets/webpack/commons-globalSearch-pages.admin.abuse_reports-pages.admin.groups.show-pages.dashboard.todos.index-p-04cd22d1.9337fc18.chunk.js" defer="defer"></script>
<script src="/gitlab/assets/webpack/shortcutsBundle.7964dc83.chunk.js" defer="defer"></script>
<script src="/gitlab/assets/webpack/commons-pages.groups.boards-pages.groups.details-pages.groups.show-pages.projects-pages.projects.act-9d92d8a2.74f14200.chunk.js" defer="defer"></script>
<script src="/gitlab/assets/webpack/commons-pages.ide-pages.projects-pages.projects.activity-pages.projects.alert_management.details-pag-adc5441c.5f3aad59.chunk.js" defer="defer"></script>
<script src="/gitlab/assets/webpack/commons-pages.projects-pages.projects.activity-pages.projects.alert_management.details-pages.project-75e2c287.82fd5473.chunk.js" defer="defer"></script>
<script src="/gitlab/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.snippets.edit-pages.projects.sni-42df7d4c.36eb4edb.chunk.js" defer="defer"></script>
<script src="/gitlab/assets/webpack/commons-pages.projects.blame.show-pages.projects.blob.edit-pages.projects.blob.new-pages.projects.bl-c6edf1dd.8b99f551.chunk.js" defer="defer"></script>
<script src="/gitlab/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.snippets.show-pages.projects.tre-c684fcf6.c5891a0f.chunk.js" defer="defer"></script>
<script src="/gitlab/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.tree.show.f02b2c37.chunk.js" defer="defer"></script>
<script src="/gitlab/assets/webpack/pages.projects.blob.show.f7e07e14.chunk.js" defer="defer"></script>
<script>
//<![CDATA[
window.uploads_path = "/gitlab/prunonos/com490-lab-course/uploads";



//]]>
</script>
<meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="CdBMrBrZscq5Qoa5s0JkZMvwXmCPtXU4tLh3i3YOSS/Em9asEbQFwl2F7IV4EvuzwT/9heLvE+PsYdBhGsLQAA==" />
<meta name="csp-nonce" />
<meta name="action-cable-url" content="/gitlab/-/cable" />
<meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport">
<meta content="#292961" name="theme-color">
<link rel="apple-touch-icon" type="image/x-icon" href="/gitlab/assets/touch-icon-iphone-5a9cee0e8a51212e70b90c87c12f382c428870c0ff67d1eb034d884b78d2dae7.png" />
<link rel="apple-touch-icon" type="image/x-icon" href="/gitlab/assets/touch-icon-ipad-a6eec6aeb9da138e507593b464fdac213047e49d3093fc30e90d9a995df83ba3.png" sizes="76x76" />
<link rel="apple-touch-icon" type="image/x-icon" href="/gitlab/assets/touch-icon-iphone-retina-72e2aadf86513a56e050e7f0f2355deaa19cc17ed97bbe5147847f2748e5a3e3.png" sizes="120x120" />
<link rel="apple-touch-icon" type="image/x-icon" href="/gitlab/assets/touch-icon-ipad-retina-8ebe416f5313483d9c1bc772b5bbe03ecad52a54eba443e5215a22caed2a16a2.png" sizes="152x152" />
<link color="rgb(226, 67, 41)" href="/gitlab/assets/logo-d36b5212042cebc89b96df4bf6ac24e43db316143e89926c0db839ff694d2de4.svg" rel="mask-icon">
<link href="/gitlab/search/opensearch.xml" rel="search" title="Search GitLab" type="application/opensearchdescription+xml">
<meta content="/gitlab/assets/msapplication-tile-1196ec67452f618d39cdd85e2e3a542f76574c071051ae7effbfde01710eb17d.png" name="msapplication-TileImage">
<meta content="#30353E" name="msapplication-TileColor">




</head>

<body class="ui-indigo tab-width-8 gl-browser-chrome gl-platform-windows" data-find-file="/gitlab/prunonos/com490-lab-course/-/find_file/master" data-namespace-id="72" data-page="projects:blob:show" data-page-type-id="master/week1/exercises-1_python-essentials.py" data-project="com490-lab-course" data-project-id="105">

<script>
//<![CDATA[
gl = window.gl || {};
gl.client = {"isChrome":true,"isWindows":true};


//]]>
</script>


<header class="navbar navbar-gitlab navbar-expand-sm js-navbar" data-qa-selector="navbar">
<a class="gl-sr-only gl-accessibility" href="#content-body">Skip to content</a>
<div class="container-fluid">
<div class="header-content">
<div class="title-container hide-when-top-nav-responsive-open">
<h1 class="title">
<span class="gl-sr-only">GitLab</span>
<a title="Dashboard" id="logo" href="/gitlab/"><svg width="24" height="24" class="tanuki-logo" viewBox="0 0 36 36">
  <path class="tanuki-shape tanuki-left-ear" fill="#e24329" d="M2 14l9.38 9v-9l-4-12.28c-.205-.632-1.176-.632-1.38 0z"/>
  <path class="tanuki-shape tanuki-right-ear" fill="#e24329" d="M34 14l-9.38 9v-9l4-12.28c.205-.632 1.176-.632 1.38 0z"/>
  <path class="tanuki-shape tanuki-nose" fill="#e24329" d="M18,34.38 3,14 33,14 Z"/>
  <path class="tanuki-shape tanuki-left-eye" fill="#fc6d26" d="M18,34.38 11.38,14 2,14 6,25Z"/>
  <path class="tanuki-shape tanuki-right-eye" fill="#fc6d26" d="M18,34.38 24.62,14 34,14 30,25Z"/>
  <path class="tanuki-shape tanuki-left-cheek" fill="#fca326" d="M2 14L.1 20.16c-.18.565 0 1.2.5 1.56l17.42 12.66z"/>
  <path class="tanuki-shape tanuki-right-cheek" fill="#fca326" d="M34 14l1.9 6.16c.18.565 0 1.2-.5 1.56L18 34.38z"/>
</svg>

<span class="logo-text d-none d-lg-block gl-ml-3">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 617 169"><path d="M315.26 2.97h-21.8l.1 162.5h88.3v-20.1h-66.5l-.1-142.4M465.89 136.95c-5.5 5.7-14.6 11.4-27 11.4-16.6 0-23.3-8.2-23.3-18.9 0-16.1 11.2-23.8 35-23.8 4.5 0 11.7.5 15.4 1.2v30.1h-.1m-22.6-98.5c-17.6 0-33.8 6.2-46.4 16.7l7.7 13.4c8.9-5.2 19.8-10.4 35.5-10.4 17.9 0 25.8 9.2 25.8 24.6v7.9c-3.5-.7-10.7-1.2-15.1-1.2-38.2 0-57.6 13.4-57.6 41.4 0 25.1 15.4 37.7 38.7 37.7 15.7 0 30.8-7.2 36-18.9l4 15.9h15.4v-83.2c-.1-26.3-11.5-43.9-44-43.9M557.63 149.1c-8.2 0-15.4-1-20.8-3.5V70.5c7.4-6.2 16.6-10.7 28.3-10.7 21.1 0 29.2 14.9 29.2 39 0 34.2-13.1 50.3-36.7 50.3m9.2-110.6c-19.5 0-30 13.3-30 13.3v-21l-.1-27.8h-21.3l.1 158.5c10.7 4.5 25.3 6.9 41.2 6.9 40.7 0 60.3-26 60.3-70.9-.1-35.5-18.2-59-50.2-59M77.9 20.6c19.3 0 31.8 6.4 39.9 12.9l9.4-16.3C114.5 6 97.3 0 78.9 0 32.5 0 0 28.3 0 85.4c0 59.8 35.1 83.1 75.2 83.1 20.1 0 37.2-4.7 48.4-9.4l-.5-63.9V75.1H63.6v20.1h38l.5 48.5c-5 2.5-13.6 4.5-25.3 4.5-32.2 0-53.8-20.3-53.8-63-.1-43.5 22.2-64.6 54.9-64.6M231.43 2.95h-21.3l.1 27.3v94.3c0 26.3 11.4 43.9 43.9 43.9 4.5 0 8.9-.4 13.1-1.2v-19.1c-3.1.5-6.4.7-9.9.7-17.9 0-25.8-9.2-25.8-24.6v-65h35.7v-17.8h-35.7l-.1-38.5M155.96 165.47h21.3v-124h-21.3v124M155.96 24.37h21.3V3.07h-21.3v21.3"/></svg>

</span>
</a></h1>
<div class="gl-display-none gl-sm-display-block">
<ul class="list-unstyled navbar-sub-nav" data-view-model="{&quot;primary&quot;:[{&quot;id&quot;:&quot;project&quot;,&quot;title&quot;:&quot;Projects&quot;,&quot;active&quot;:true,&quot;icon&quot;:&quot;project&quot;,&quot;href&quot;:&quot;&quot;,&quot;view&quot;:&quot;projects&quot;,&quot;css_class&quot;:&quot;qa-projects-dropdown&quot;,&quot;data&quot;:{&quot;track_label&quot;:&quot;projects_dropdown&quot;,&quot;track_action&quot;:&quot;click_dropdown&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;groups&quot;,&quot;title&quot;:&quot;Groups&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;group&quot;,&quot;href&quot;:&quot;&quot;,&quot;view&quot;:&quot;groups&quot;,&quot;css_class&quot;:&quot;qa-groups-dropdown&quot;,&quot;data&quot;:{&quot;track_label&quot;:&quot;groups_dropdown&quot;,&quot;track_action&quot;:&quot;click_dropdown&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;milestones&quot;,&quot;title&quot;:&quot;Milestones&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;clock&quot;,&quot;href&quot;:&quot;/gitlab/dashboard/milestones&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;milestones_link&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;snippets&quot;,&quot;title&quot;:&quot;Snippets&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;snippet&quot;,&quot;href&quot;:&quot;/gitlab/dashboard/snippets&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;snippets_link&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;activity&quot;,&quot;title&quot;:&quot;Activity&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;history&quot;,&quot;href&quot;:&quot;/gitlab/dashboard/activity&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;activity_link&quot;},&quot;emoji&quot;:null}],&quot;secondary&quot;:[],&quot;views&quot;:{&quot;projects&quot;:{&quot;namespace&quot;:&quot;projects&quot;,&quot;currentUserName&quot;:&quot;prunonos&quot;,&quot;currentItem&quot;:{&quot;id&quot;:105,&quot;name&quot;:&quot;com490-lab-course&quot;,&quot;namespace&quot;:&quot;Guillem Pruñonosa Soler / com490-lab-course&quot;,&quot;webUrl&quot;:&quot;/gitlab/prunonos/com490-lab-course&quot;,&quot;avatarUrl&quot;:null},&quot;linksPrimary&quot;:[{&quot;id&quot;:&quot;your&quot;,&quot;title&quot;:&quot;Your projects&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/dashboard/projects&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Your projects&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;starred&quot;,&quot;title&quot;:&quot;Starred projects&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/dashboard/projects/starred&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Starred projects&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;explore&quot;,&quot;title&quot;:&quot;Explore projects&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/explore&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Explore projects&quot;},&quot;emoji&quot;:null}],&quot;linksSecondary&quot;:[{&quot;id&quot;:&quot;create&quot;,&quot;title&quot;:&quot;Create new project&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/projects/new&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Create new project&quot;},&quot;emoji&quot;:null}]},&quot;groups&quot;:{&quot;namespace&quot;:&quot;groups&quot;,&quot;currentUserName&quot;:&quot;prunonos&quot;,&quot;currentItem&quot;:{},&quot;linksPrimary&quot;:[{&quot;id&quot;:&quot;your&quot;,&quot;title&quot;:&quot;Your groups&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/dashboard/groups&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Your groups&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;explore&quot;,&quot;title&quot;:&quot;Explore groups&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/explore/groups&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Explore groups&quot;},&quot;emoji&quot;:null}],&quot;linksSecondary&quot;:[{&quot;id&quot;:&quot;create&quot;,&quot;title&quot;:&quot;Create group&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/groups/new&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Create group&quot;},&quot;emoji&quot;:null}]}},&quot;shortcuts&quot;:[{&quot;id&quot;:&quot;project-shortcut&quot;,&quot;title&quot;:&quot;Projects&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/dashboard/projects&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-projects&quot;,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Projects&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;groups-shortcut&quot;,&quot;title&quot;:&quot;Groups&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/dashboard/groups&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-groups&quot;,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Groups&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;milestones-shortcut&quot;,&quot;title&quot;:&quot;Milestones&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/dashboard/milestones&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-milestones&quot;,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Milestones&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;snippets-shortcut&quot;,&quot;title&quot;:&quot;Snippets&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/dashboard/snippets&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-snippets&quot;,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Snippets&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;activity-shortcut&quot;,&quot;title&quot;:&quot;Activity&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/dashboard/activity&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-activity&quot;,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Activity&quot;},&quot;emoji&quot;:null}],&quot;activeTitle&quot;:&quot;Menu&quot;}" id="js-top-nav">
<li>
<a class="top-nav-toggle" data-toggle="dropdown" href="#" type="button">
<svg class="s16 dropdown-icon" data-testid="hamburger-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#hamburger"></use></svg>
Menu
</a>
</li>
</ul>
<div class="hidden">
<a class="dashboard-shortcuts-projects" href="/gitlab/dashboard/projects">Projects
</a><a class="dashboard-shortcuts-groups" href="/gitlab/dashboard/groups">Groups
</a><a class="dashboard-shortcuts-milestones" href="/gitlab/dashboard/milestones">Milestones
</a><a class="dashboard-shortcuts-snippets" href="/gitlab/dashboard/snippets">Snippets
</a><a class="dashboard-shortcuts-activity" href="/gitlab/dashboard/activity">Activity
</a></div>

</div>
</div>
<div class="navbar-collapse collapse">
<ul class="nav navbar-nav">
<li class="header-new dropdown gl-display-none gl-sm-display-block" data-track-action="click_dropdown" data-track-label="new_dropdown">
<a class="header-new-dropdown-toggle has-tooltip" id="js-onboarding-new-project-link" title="New..." ref="tooltip" aria-label="New..." data-toggle="dropdown" data-placement="bottom" data-container="body" data-display="static" data-qa-selector="new_menu_toggle" href="/gitlab/projects/new"><svg class="s16" data-testid="plus-square-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#plus-square"></use></svg>
<svg class="s16 caret-down" data-testid="chevron-down-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#chevron-down"></use></svg>
</a><div class="dropdown-menu dropdown-menu-right dropdown-extended-height">
<ul>
<li class="dropdown-bold-header">
This project
</li>
<li><a data-track-action="click_link_new_issue" data-track-label="plus_menu_dropdown" data-qa-selector="new_issue_link" href="/gitlab/prunonos/com490-lab-course/-/issues/new">New issue</a></li>
<li><a data-track-action="click_link_new_mr" data-track-label="plus_menu_dropdown" href="/gitlab/prunonos/com490-lab-course/-/merge_requests/new">New merge request</a></li>
<li><a data-track-action="click_link_new_snippet_project" data-track-label="plus_menu_dropdown" href="/gitlab/prunonos/com490-lab-course/-/snippets/new">New snippet</a></li>
<li class="divider"></li>
<li class="dropdown-bold-header">
GitLab
</li>
<li><a data-track-action="click_link_new_project" data-track-label="plus_menu_dropdown" data-qa-selector="global_new_project_link" href="/gitlab/projects/new">New project/repository</a></li>
<li><a data-track-action="click_link_new_group" data-track-label="plus_menu_dropdown" href="/gitlab/groups/new">New group</a></li>
<li><a data-track-action="click_link_new_snippet_parent" data-track-label="plus_menu_dropdown" data-qa-selector="global_new_snippet_link" href="/gitlab/-/snippets/new">New snippet</a></li>
</ul>
</div>
</li>

<li class="nav-item d-none d-lg-block m-auto">
<div class="search search-form" data-track-action="activate_form_input" data-track-label="navbar_search" data-track-value="">
<form class="form-inline form-control" action="/gitlab/search" accept-charset="UTF-8" method="get"><div class="search-input-container">
<div class="search-input-wrap">
<div class="dropdown" data-url="/gitlab/search/autocomplete">
<input type="search" name="search" id="search" placeholder="Search GitLab" class="search-input dropdown-menu-toggle no-outline js-search-dashboard-options" spellcheck="false" autocomplete="off" data-issues-path="/gitlab/dashboard/issues" data-mr-path="/gitlab/dashboard/merge_requests" data-qa-selector="search_term_field" aria-label="Search GitLab" />
<button class="hidden js-dropdown-search-toggle" data-toggle="dropdown" type="button"></button>
<div class="dropdown-menu dropdown-select" data-testid="dashboard-search-options">
<div class="dropdown-content"><ul>
<li class="dropdown-menu-empty-item">
<a>
Loading...
</a>
</li>
</ul>
</div><div class="dropdown-loading"><div class="gl-spinner-container"><span class="gl-spinner gl-spinner-orange gl-spinner-md gl-mt-7" aria-label="Loading"></span></div></div>
</div>
<svg class="s16 search-icon" data-testid="search-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#search"></use></svg>
<svg class="s16 clear-icon js-clear-input" data-testid="close-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#close"></use></svg>
</div>
</div>
</div>
<input type="hidden" name="group_id" id="group_id" value="" class="js-search-group-options" />
<input type="hidden" name="project_id" id="search_project_id" value="105" class="js-search-project-options" data-project-path="com490-lab-course" data-name="com490-lab-course" data-issues-path="/gitlab/prunonos/com490-lab-course/-/issues" data-mr-path="/gitlab/prunonos/com490-lab-course/-/merge_requests" data-issues-disabled="false" />
<input type="hidden" name="scope" id="scope" />
<input type="hidden" name="search_code" id="search_code" value="true" />
<input type="hidden" name="snippets" id="snippets" value="false" />
<input type="hidden" name="repository_ref" id="repository_ref" value="master" />
<input type="hidden" name="nav_source" id="nav_source" value="navbar" />
<div class="search-autocomplete-opts hide" data-autocomplete-path="/gitlab/search/autocomplete" data-autocomplete-project-id="105" data-autocomplete-project-ref="master"></div>
</form></div>

</li>
<li class="nav-item d-none d-sm-inline-block d-lg-none">
<a title="Search" aria-label="Search" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/gitlab/search?project_id=105"><svg class="s16" data-testid="search-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#search"></use></svg>
</a></li>
<li class="user-counter"><a title="Issues" class="dashboard-shortcuts-issues" aria-label="Issues" data-qa-selector="issues_shortcut_button" data-toggle="tooltip" data-placement="bottom" data-track-label="main_navigation" data-track-action="click_issues_link" data-track-property="navigation" data-container="body" href="/gitlab/dashboard/issues?assignee_username=prunonos"><svg class="s16" data-testid="issues-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#issues"></use></svg>
<span class="badge badge-pill issues-count green-badge hidden">
0
</span>
</a></li><li class="user-counter dropdown"><a class="dashboard-shortcuts-merge_requests" title="Merge requests" aria-label="Merge requests" data-qa-selector="merge_requests_shortcut_button" data-toggle="dropdown" data-placement="bottom" data-track-label="main_navigation" data-track-action="click_merge_link" data-track-property="navigation" data-container="body" href="/gitlab/dashboard/merge_requests?assignee_username=prunonos"><svg class="s16" data-testid="git-merge-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#git-merge"></use></svg>
<span class="badge badge-pill merge-requests-count js-merge-requests-count hidden">
0
</span>
<svg class="s16 caret-down gl-mx-0!" data-testid="chevron-down-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#chevron-down"></use></svg>
</a><div class="dropdown-menu dropdown-menu-right">
<ul>
<li class="dropdown-header">
Merge requests
</li>
<li>
<a class="gl-display-flex! gl-align-items-center" href="/gitlab/dashboard/merge_requests?assignee_username=prunonos">Assigned to you
<span class="badge gl-badge badge-pill badge-muted merge-request-badge gl-ml-auto js-assigned-mr-count">
0
</span>
</a></li>
<li>
<a class="gl-display-flex! gl-align-items-center" href="/gitlab/dashboard/merge_requests?reviewer_username=prunonos">Review requests for you
<span class="badge gl-badge badge-pill badge-muted merge-request-badge gl-ml-auto js-reviewer-mr-count">
0
</span>
</a></li>
</ul>
</div>
</li><li class="user-counter"><a title="To-Do List" aria-label="To-Do List" class="shortcuts-todos" data-qa-selector="todos_shortcut_button" data-toggle="tooltip" data-placement="bottom" data-track-label="main_navigation" data-track-action="click_to_do_link" data-track-property="navigation" data-container="body" href="/gitlab/dashboard/todos"><svg class="s16" data-testid="todo-done-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#todo-done"></use></svg>
<span class="badge badge-pill todos-count js-todos-count hidden">
0
</span>
</a></li><li class="nav-item header-help dropdown d-none d-md-block">
<a class="header-help-dropdown-toggle" data-toggle="dropdown" href="/gitlab/help"><span class="gl-sr-only">
Help
</span>
<svg class="s16" data-testid="question-o-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#question-o"></use></svg>
<span class="notification-dot rounded-circle gl-absolute"></span>
<svg class="s16 caret-down" data-testid="chevron-down-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#chevron-down"></use></svg>
</a><div class="dropdown-menu dropdown-menu-right">
<ul>
<li>
<button class="gl-justify-content-space-between gl-align-items-center js-whats-new-trigger gl-display-flex!" type="button">
What&#39;s new
<span class="js-whats-new-notification-count gl-badge badge sm badge-dark badge-pill">
5
</span>
</button>
</li>

<li>
<a href="/gitlab/help">Help</a>
</li>
<li>
<a href="https://about.gitlab.com/getting-help/">Support</a>
</li>
<li>
<a target="_blank" class="text-nowrap" rel="noopener noreferrer" data-track-action="click_forum" data-track-property="question_menu" href="https://forum.gitlab.com/">Community forum</a>

</li>
<li>
<button class="js-shortcuts-modal-trigger" type="button">
Keyboard shortcuts
<span aria-hidden="true" class="text-secondary float-right">?</span>
</button>
</li>
<li class="divider"></li>
<li>
<a href="https://about.gitlab.com/submit-feedback">Submit feedback</a>
</li>
<li>
<a target="_blank" class="text-nowrap" href="https://about.gitlab.com/contributing">Contribute to GitLab
</a>
</li>

</ul>

</div>
</li>
<li class="nav-item header-user js-nav-user-dropdown dropdown" data-qa-selector="user_menu" data-track-action="click_dropdown" data-track-label="profile_dropdown" data-track-value="">
<a class="header-user-dropdown-toggle" data-toggle="dropdown" href="/gitlab/prunonos"><img width="23" height="23" class="header-user-avatar qa-user-avatar lazy" alt="Guillem Pruñonosa Soler" data-src="https://secure.gravatar.com/avatar/4c73ce167ffa00867a43a4450e07ceb5?s=46&amp;d=identicon" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" />

<svg class="s16 caret-down" data-testid="chevron-down-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#chevron-down"></use></svg>
</a><div class="dropdown-menu dropdown-menu-right">
<ul>
<li class="current-user">
<a class="gl-line-height-20!" data-user="prunonos" data-testid="user-profile-link" data-qa-selector="user_profile_link" href="/gitlab/prunonos"><div class="gl-font-weight-bold">
Guillem Pruñonosa Soler
</div>
@prunonos

</a></li>
<li class="divider"></li>
<li>
<button class="gl-button btn btn-link menu-item js-set-status-modal-trigger" type="button">
Set status
</button>
</li>
<li>
<a data-qa-selector="edit_profile_link" href="/gitlab/-/profile">Edit profile</a>
</li>
<li>
<a href="/gitlab/-/profile/preferences">Preferences</a>
</li>


<li class="divider d-md-none"></li>
<li class="d-md-none">
<a href="/gitlab/help">Help</a>
</li>
<li class="d-md-none">
<a href="https://about.gitlab.com/getting-help/">Support</a>
</li>
<li class="d-md-none">
<a target="_blank" class="text-nowrap" rel="noopener noreferrer" data-track-action="click_forum" data-track-property="question_menu" href="https://forum.gitlab.com/">Community forum</a>

</li>
<li class="d-md-none">
<a href="https://about.gitlab.com/submit-feedback">Submit feedback</a>
</li>
<li class="d-md-none">
<a target="_blank" class="text-nowrap" href="https://about.gitlab.com/contributing">Contribute to GitLab
</a>
</li>

<li class="divider"></li>
<li>
<a class="sign-out-link" data-qa-selector="sign_out_link" rel="nofollow" data-method="post" href="/gitlab/users/sign_out">Sign out</a>
</li>
</ul>

</div>
</li>
</ul>
</div>
<button class="navbar-toggler d-block d-sm-none gl-border-none!" data-testid="top-nav-responsive-toggle" type="button">
<span class="sr-only">Toggle navigation</span>
<span class="more-icon gl-px-3 gl-font-sm gl-font-weight-bold">
<span class="gl-pr-2">Menu</span>
<svg class="s16" data-testid="hamburger-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#hamburger"></use></svg>
</span>
<svg class="s12 close-icon" data-testid="close-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#close"></use></svg>
</button>
</div>
</div>
</header>
<div data-version-digest="ffb3e073d21fac9ea71d50d78d09c45b6e74a6951290e405777a17df3165523a" id="whats-new-app"></div>
<div class="js-set-status-modal-wrapper" data-current-emoji="" data-current-message="" data-default-emoji="speech_balloon"></div>

<div class="layout-page hide-when-top-nav-responsive-open page-with-contextual-sidebar">
<aside aria-label="Project navigation" class="nav-sidebar">
<div class="nav-sidebar-inner-scroll">
<ul class="sidebar-top-level-items" data-qa-selector="project_sidebar">
<li data-track-label="scope_menu" data-container="body" data-placement="right" class="context-header has-tooltip" title="com490-lab-course"><a aria-label="com490-lab-course" class="shortcuts-project rspec-project-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Project scope" href="/gitlab/prunonos/com490-lab-course"><span class="avatar-container rect-avatar s32 project_avatar">
<span class="avatar avatar-tile s32 identicon bg1">C</span>
</span>
<span class="sidebar-context-title">
com490-lab-course
</span>
</a></li>
<li data-track-label="project_information_menu" class="home"><a aria-label="Project information" class="shortcuts-project-information has-sub-items" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Project information" href="/gitlab/prunonos/com490-lab-course/activity"><span class="nav-icon-container">
<svg class="s16" data-testid="project-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#project"></use></svg>
</span>
<span class="nav-item-name">
Project information
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Project information
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="activity" class=""><a aria-label="Activity" class="shortcuts-project-activity" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Activity" href="/gitlab/prunonos/com490-lab-course/activity"><span>
Activity
</span>
</a></li><li data-track-label="labels" class=""><a aria-label="Labels" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Labels" href="/gitlab/prunonos/com490-lab-course/-/labels"><span>
Labels
</span>
</a></li><li data-track-label="members" class=""><a aria-label="Members" id="js-onboarding-members-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Members" href="/gitlab/prunonos/com490-lab-course/-/project_members"><span>
Members
</span>
</a></li>
</ul>
</li><li data-track-label="repository_menu" class="active"><a aria-label="Repository" class="shortcuts-tree has-sub-items" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Repository" href="/gitlab/prunonos/com490-lab-course/-/tree/master"><span class="nav-icon-container">
<svg class="s16" data-testid="doc-text-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#doc-text"></use></svg>
</span>
<span class="nav-item-name" id="js-onboarding-repo-link">
Repository
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item active"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Repository
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="files" class="active"><a aria-label="Files" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Files" href="/gitlab/prunonos/com490-lab-course/-/tree/master"><span>
Files
</span>
</a></li><li data-track-label="commits" class=""><a aria-label="Commits" id="js-onboarding-commits-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Commits" href="/gitlab/prunonos/com490-lab-course/-/commits/master"><span>
Commits
</span>
</a></li><li data-track-label="branches" class=""><a aria-label="Branches" id="js-onboarding-branches-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Branches" href="/gitlab/prunonos/com490-lab-course/-/branches"><span>
Branches
</span>
</a></li><li data-track-label="tags" class=""><a aria-label="Tags" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Tags" href="/gitlab/prunonos/com490-lab-course/-/tags"><span>
Tags
</span>
</a></li><li data-track-label="contributors" class=""><a aria-label="Contributors" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Contributors" href="/gitlab/prunonos/com490-lab-course/-/graphs/master"><span>
Contributors
</span>
</a></li><li data-track-label="graphs" class=""><a aria-label="Graph" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Graph" href="/gitlab/prunonos/com490-lab-course/-/network/master"><span>
Graph
</span>
</a></li><li data-track-label="compare" class=""><a aria-label="Compare" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Compare" href="/gitlab/prunonos/com490-lab-course/-/compare?from=master&amp;to=master"><span>
Compare
</span>
</a></li>
</ul>
</li><li data-track-label="issues_menu" class=""><a aria-label="Issues" class="shortcuts-issues has-sub-items" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Issues" href="/gitlab/prunonos/com490-lab-course/-/issues"><span class="nav-icon-container">
<svg class="s16" data-testid="issues-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#issues"></use></svg>
</span>
<span class="nav-item-name" id="js-onboarding-issues-link">
Issues
</span>
<span class="badge badge-pill count issue_counter">
0
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Issues
</strong>
<span class="badge badge-pill count fly-out-badge issue_counter">
0
</span>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="issue_list" class=""><a aria-label="Issues" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="List" href="/gitlab/prunonos/com490-lab-course/-/issues"><span>
List
</span>
</a></li><li data-track-label="boards" class=""><a aria-label="Boards" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Boards" href="/gitlab/prunonos/com490-lab-course/-/boards"><span>
Boards
</span>
</a></li><li data-track-label="service_desk" class=""><a aria-label="Service Desk" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Service Desk" href="/gitlab/prunonos/com490-lab-course/-/issues/service_desk"><span>
Service Desk
</span>
</a></li><li data-track-label="milestones" class=""><a aria-label="Milestones" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Milestones" href="/gitlab/prunonos/com490-lab-course/-/milestones"><span>
Milestones
</span>
</a></li>
</ul>
</li><li data-track-label="merge_requests_menu" class=""><a aria-label="Merge requests" class="shortcuts-merge_requests" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Merge requests" href="/gitlab/prunonos/com490-lab-course/-/merge_requests"><span class="nav-icon-container">
<svg class="s16" data-testid="git-merge-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#git-merge"></use></svg>
</span>
<span class="nav-item-name" id="js-onboarding-mr-link">
Merge requests
</span>
<span class="badge badge-pill count merge_counter js-merge-counter">
0
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Merge requests
</strong>
<span class="badge badge-pill count fly-out-badge merge_counter js-merge-counter">
0
</span>
</span>
</li></ul>
</li><li data-track-label="ci_cd_menu" class=""><a aria-label="CI/CD" class="shortcuts-pipelines rspec-link-pipelines has-sub-items" data-qa-selector="sidebar_menu_link" data-qa-menu-item="CI/CD" href="/gitlab/prunonos/com490-lab-course/-/pipelines"><span class="nav-icon-container">
<svg class="s16" data-testid="rocket-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#rocket"></use></svg>
</span>
<span class="nav-item-name" id="js-onboarding-pipelines-link">
CI/CD
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
CI/CD
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="pipelines" class=""><a aria-label="Pipelines" class="shortcuts-pipelines" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Pipelines" href="/gitlab/prunonos/com490-lab-course/-/pipelines"><span>
Pipelines
</span>
</a></li><li data-track-label="pipelines_editor" class=""><a aria-label="Editor" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Editor" href="/gitlab/prunonos/com490-lab-course/-/ci/editor"><span>
Editor
</span>
</a></li><li data-track-label="jobs" class=""><a aria-label="Jobs" class="shortcuts-builds" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Jobs" href="/gitlab/prunonos/com490-lab-course/-/jobs"><span>
Jobs
</span>
</a></li><li data-track-label="pipeline_schedules" class=""><a aria-label="Schedules" class="shortcuts-builds" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Schedules" href="/gitlab/prunonos/com490-lab-course/-/pipeline_schedules"><span>
Schedules
</span>
</a></li>
</ul>
</li><li data-track-label="security_compliance_menu" class=""><a aria-label="Security &amp; Compliance" class="has-sub-items" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Security &amp; Compliance" href="/gitlab/prunonos/com490-lab-course/-/security/configuration"><span class="nav-icon-container">
<svg class="s16" data-testid="shield-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#shield"></use></svg>
</span>
<span class="nav-item-name">
Security &amp; Compliance
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Security &amp; Compliance
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="configuration" class=""><a aria-label="Configuration" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Configuration" href="/gitlab/prunonos/com490-lab-course/-/security/configuration"><span>
Configuration
</span>
</a></li>
</ul>
</li><li data-track-label="deployments_menu" class=""><a aria-label="Deployments" class="shortcuts-deployments has-sub-items" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Deployments" href="/gitlab/prunonos/com490-lab-course/-/feature_flags"><span class="nav-icon-container">
<svg class="s16" data-testid="deployments-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#deployments"></use></svg>
</span>
<span class="nav-item-name">
Deployments
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Deployments
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="feature_flags" class=""><a aria-label="Feature Flags" class="shortcuts-feature-flags" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Feature Flags" href="/gitlab/prunonos/com490-lab-course/-/feature_flags"><span>
Feature Flags
</span>
</a></li><li data-track-label="environments" class=""><a aria-label="Environments" class="shortcuts-environments" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Environments" href="/gitlab/prunonos/com490-lab-course/-/environments"><span>
Environments
</span>
</a></li><li data-track-label="releases" class=""><a aria-label="Releases" class="shortcuts-deployments-releases" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Releases" href="/gitlab/prunonos/com490-lab-course/-/releases"><span>
Releases
</span>
</a></li>
</ul>
</li><li data-track-label="monitor_menu" class=""><a aria-label="Monitor" class="shortcuts-monitor has-sub-items" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Monitor" href="/gitlab/prunonos/com490-lab-course/-/metrics"><span class="nav-icon-container">
<svg class="s16" data-testid="monitor-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#monitor"></use></svg>
</span>
<span class="nav-item-name">
Monitor
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Monitor
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="metrics" class=""><a aria-label="Metrics" class="shortcuts-metrics" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Metrics" href="/gitlab/prunonos/com490-lab-course/-/metrics"><span>
Metrics
</span>
</a></li><li data-track-label="logs" class=""><a aria-label="Logs" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Logs" href="/gitlab/prunonos/com490-lab-course/-/logs"><span>
Logs
</span>
</a></li><li data-track-label="tracing" class=""><a aria-label="Tracing" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Tracing" href="/gitlab/prunonos/com490-lab-course/-/tracing"><span>
Tracing
</span>
</a></li><li data-track-label="error_tracking" class=""><a aria-label="Error Tracking" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Error Tracking" href="/gitlab/prunonos/com490-lab-course/-/error_tracking"><span>
Error Tracking
</span>
</a></li><li data-track-label="alert_management" class=""><a aria-label="Alerts" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Alerts" href="/gitlab/prunonos/com490-lab-course/-/alert_management"><span>
Alerts
</span>
</a></li><li data-track-label="incidents" class=""><a aria-label="Incidents" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Incidents" href="/gitlab/prunonos/com490-lab-course/-/incidents"><span>
Incidents
</span>
</a></li>
</ul>
</li><li data-track-label="infrastructure_menu" class=""><a aria-label="Infrastructure" class="shortcuts-infrastructure has-sub-items" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Infrastructure" href="/gitlab/prunonos/com490-lab-course/-/clusters"><span class="nav-icon-container">
<svg class="s16" data-testid="cloud-gear-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#cloud-gear"></use></svg>
</span>
<span class="nav-item-name">
Infrastructure
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Infrastructure
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="kubernetes" class=""><a aria-label="Kubernetes clusters" class="shortcuts-kubernetes" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Kubernetes clusters" href="/gitlab/prunonos/com490-lab-course/-/clusters"><span>
Kubernetes clusters
</span>
</a></li><li data-track-label="serverless" class=""><a aria-label="Serverless platform" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Serverless platform" href="/gitlab/prunonos/com490-lab-course/-/serverless/functions"><span>
Serverless platform
</span>
</a></li><li data-track-label="terraform" class=""><a aria-label="Terraform" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Terraform" href="/gitlab/prunonos/com490-lab-course/-/terraform"><span>
Terraform
</span>
</a></li>
</ul>
</li><li data-track-label="packages_registries_menu" class=""><a aria-label="Packages &amp; Registries" class="has-sub-items" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Packages &amp; Registries" href="/gitlab/prunonos/com490-lab-course/-/packages"><span class="nav-icon-container">
<svg class="s16" data-testid="package-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#package"></use></svg>
</span>
<span class="nav-item-name">
Packages &amp; Registries
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Packages &amp; Registries
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="packages_registry" class=""><a aria-label="Package Registry" class="shortcuts-container-registry" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Package Registry" href="/gitlab/prunonos/com490-lab-course/-/packages"><span>
Package Registry
</span>
</a></li><li data-track-label="container_registry" class=""><a aria-label="Container Registry" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Container Registry" href="/gitlab/prunonos/com490-lab-course/container_registry"><span>
Container Registry
</span>
</a></li><li data-track-label="infrastructure_registry" class=""><a aria-label="Infrastructure Registry" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Infrastructure Registry" href="/gitlab/prunonos/com490-lab-course/-/infrastructure_registry"><span>
Infrastructure Registry
</span>
</a></li>
</ul>
</li><li data-track-label="analytics_menu" class=""><a aria-label="Analytics" class="shortcuts-analytics has-sub-items" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Analytics" href="/gitlab/prunonos/com490-lab-course/-/value_stream_analytics"><span class="nav-icon-container">
<svg class="s16" data-testid="chart-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#chart"></use></svg>
</span>
<span class="nav-item-name">
Analytics
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Analytics
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="ci_cd_analytics" class=""><a aria-label="CI/CD" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="CI/CD" href="/gitlab/prunonos/com490-lab-course/-/pipelines/charts"><span>
CI/CD
</span>
</a></li><li data-track-label="repository_analytics" class=""><a aria-label="Repository" class="shortcuts-repository-charts" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Repository" href="/gitlab/prunonos/com490-lab-course/-/graphs/master/charts"><span>
Repository
</span>
</a></li><li data-track-label="cycle_analytics" class=""><a aria-label="Value stream" class="shortcuts-project-cycle-analytics" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Value stream" href="/gitlab/prunonos/com490-lab-course/-/value_stream_analytics"><span>
Value stream
</span>
</a></li>
</ul>
</li><li data-track-label="wiki_menu" class=""><a aria-label="Wiki" class="shortcuts-wiki" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Wiki" href="/gitlab/prunonos/com490-lab-course/-/wikis/home"><span class="nav-icon-container">
<svg class="s16" data-testid="book-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#book"></use></svg>
</span>
<span class="nav-item-name">
Wiki
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Wiki
</strong>
</span>
</li></ul>
</li><li data-track-label="snippets_menu" class=""><a aria-label="Snippets" class="shortcuts-snippets" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Snippets" href="/gitlab/prunonos/com490-lab-course/-/snippets"><span class="nav-icon-container">
<svg class="s16" data-testid="snippet-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#snippet"></use></svg>
</span>
<span class="nav-item-name">
Snippets
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Snippets
</strong>
</span>
</li></ul>
</li><li data-track-label="settings_menu" class=""><a aria-label="Settings" class="has-sub-items" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Settings" href="/gitlab/prunonos/com490-lab-course/edit"><span class="nav-icon-container">
<svg class="s16" data-testid="settings-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#settings"></use></svg>
</span>
<span class="nav-item-name" id="js-onboarding-settings-link">
Settings
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Settings
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="general" class=""><a aria-label="General" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="General" href="/gitlab/prunonos/com490-lab-course/edit"><span>
General
</span>
</a></li><li data-track-label="integrations" class=""><a aria-label="Integrations" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Integrations" href="/gitlab/prunonos/com490-lab-course/-/settings/integrations"><span>
Integrations
</span>
</a></li><li data-track-label="webhooks" class=""><a aria-label="Webhooks" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Webhooks" href="/gitlab/prunonos/com490-lab-course/-/hooks"><span>
Webhooks
</span>
</a></li><li data-track-label="access_tokens" class=""><a aria-label="Access Tokens" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Access Tokens" href="/gitlab/prunonos/com490-lab-course/-/settings/access_tokens"><span>
Access Tokens
</span>
</a></li><li data-track-label="repository" class=""><a aria-label="Repository" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Repository" href="/gitlab/prunonos/com490-lab-course/-/settings/repository"><span>
Repository
</span>
</a></li><li data-track-label="ci_cd" class=""><a aria-label="CI/CD" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="CI/CD" href="/gitlab/prunonos/com490-lab-course/-/settings/ci_cd"><span>
CI/CD
</span>
</a></li><li data-track-label="monitor" class=""><a aria-label="Monitor" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Monitor" href="/gitlab/prunonos/com490-lab-course/-/settings/operations"><span>
Monitor
</span>
</a></li><li data-track-label="packages_and_registries" class=""><a aria-label="Packages &amp; Registries" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Packages &amp; Registries" href="/gitlab/prunonos/com490-lab-course/-/settings/packages_and_registries"><span>
Packages &amp; Registries
</span>
</a></li>
</ul>
</li>
<li class="hidden">
<a aria-label="Activity" class="shortcuts-project-activity" href="/gitlab/prunonos/com490-lab-course/activity">Activity
</a></li>
<li class="hidden">
<a aria-label="Graph" class="shortcuts-network" href="/gitlab/prunonos/com490-lab-course/-/network/master">Graph
</a></li>
<li class="hidden">
<a aria-label="Create a new issue" class="shortcuts-new-issue" href="/gitlab/prunonos/com490-lab-course/-/issues/new">Create a new issue
</a></li>
<li class="hidden">
<a aria-label="Jobs" class="shortcuts-builds" href="/gitlab/prunonos/com490-lab-course/-/jobs">Jobs
</a></li>
<li class="hidden">
<a aria-label="Commits" class="shortcuts-commits" href="/gitlab/prunonos/com490-lab-course/-/commits/master">Commits
</a></li>
<li class="hidden">
<a aria-label="Issue Boards" class="shortcuts-issue-boards" href="/gitlab/prunonos/com490-lab-course/-/boards">Issue Boards
</a></li>

</ul>
<a class="toggle-sidebar-button js-toggle-sidebar qa-toggle-sidebar rspec-toggle-sidebar" role="button" title="Toggle sidebar" type="button">
<svg class="s16 icon-chevron-double-lg-left" data-testid="chevron-double-lg-left-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#chevron-double-lg-left"></use></svg>
<span class="collapse-text gl-ml-3">Collapse sidebar</span>
</a>
<button name="button" type="button" class="close-nav-button"><svg class="s16" data-testid="close-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#close"></use></svg>
<span class="collapse-text gl-ml-3">Close sidebar</span>
</button>
</div>
</aside>


<div class="content-wrapper content-wrapper-margin">
<div class="mobile-overlay"></div>

<div class="alert-wrapper gl-force-block-formatting-context">

















<nav aria-label="Breadcrumbs" class="breadcrumbs container-fluid container-limited project-highlight-puc">
<div class="breadcrumbs-container">
<button name="button" type="button" class="toggle-mobile-nav"><span class="sr-only">Open sidebar</span>
<svg class="s18" data-testid="hamburger-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#hamburger"></use></svg>
</button><div class="breadcrumbs-links" data-qa-selector="breadcrumb_links_content" data-testid="breadcrumb-links">
<ul class="list-unstyled breadcrumbs-list js-breadcrumbs-list">
<li><a href="/gitlab/prunonos">Guillem Pruñonosa Soler</a><svg class="s8 breadcrumbs-list-angle" data-testid="angle-right-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#angle-right"></use></svg></li> <li><a href="/gitlab/prunonos/com490-lab-course"><span class="breadcrumb-item-text js-breadcrumb-item-text">com490-lab-course</span></a><svg class="s8 breadcrumbs-list-angle" data-testid="angle-right-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#angle-right"></use></svg></li>

<li>
<h2 class="breadcrumbs-sub-title" data-qa-selector="breadcrumb_sub_title_content">
<a href="/gitlab/prunonos/com490-lab-course/-/blob/master/week1/exercises-1_python-essentials.py">Repository</a>
</h2>
</li>
</ul>
</div>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Guillem Pruñonosa Soler","item":"https://dslab2022-renku.epfl.ch/gitlab/prunonos"},{"@type":"ListItem","position":2,"name":"com490-lab-course","item":"https://dslab2022-renku.epfl.ch/gitlab/prunonos/com490-lab-course"},{"@type":"ListItem","position":3,"name":"Repository","item":"https://dslab2022-renku.epfl.ch/gitlab/prunonos/com490-lab-course/-/blob/master/week1/exercises-1_python-essentials.py"}]}

</script>

</div>
</nav>

</div>
<div class="container-fluid container-limited project-highlight-puc">
<main class="content" id="content-body" itemscope itemtype="http://schema.org/SoftwareSourceCode">
<div class="flash-container flash-container-page sticky" data-qa-selector="flash_container">
</div>


<div class="js-signature-container" data-signatures-path="/gitlab/prunonos/com490-lab-course/-/commits/9fbc8c76390458e268685d4cebed35f5381e3095/signatures?limit=1"></div>

<div class="tree-holder" id="tree-holder">
<div class="nav-block">
<div class="tree-ref-container">
<div class="tree-ref-holder">
<form class="project-refs-form" action="/gitlab/prunonos/com490-lab-course/-/refs/switch" accept-charset="UTF-8" method="get"><input type="hidden" name="destination" id="destination" value="blob" />
<input type="hidden" name="path" id="path" value="week1/exercises-1_python-essentials.py" />
<div class="dropdown">
<button class="dropdown-menu-toggle js-project-refs-dropdown qa-branches-select" type="button" data-toggle="dropdown" data-selected="master" data-ref="master" data-refs-url="/gitlab/prunonos/com490-lab-course/refs?sort=updated_desc" data-field-name="ref" data-submit-form-on-click="true" data-visit="true"><span class="dropdown-toggle-text ">master</span><svg class="s16 dropdown-menu-toggle-icon gl-top-3" data-testid="chevron-down-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#chevron-down"></use></svg></button>
<div class="dropdown-menu dropdown-menu-selectable git-revision-dropdown dropdown-menu-paging qa-branches-dropdown">
<div class="dropdown-page-one">
<div class="dropdown-title gl-display-flex"><span class="gl-ml-auto">Switch branch/tag</span><button class="dropdown-title-button dropdown-menu-close gl-ml-auto" aria-label="Close" type="button"><svg class="s16 dropdown-menu-close-icon" data-testid="close-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#close"></use></svg></button></div>
<div class="dropdown-input"><input type="search" data-qa-selector="dropdown_input_field" class="dropdown-input-field" placeholder="Search branches and tags" autocomplete="off" /><svg class="s16 dropdown-input-search" data-testid="search-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#search"></use></svg><svg class="s16 dropdown-input-clear js-dropdown-input-clear" data-testid="close-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#close"></use></svg></div>
<div class="dropdown-content"></div>
<div class="dropdown-loading"><div class="gl-spinner-container"><span class="gl-spinner gl-spinner-orange gl-spinner-md gl-mt-7" aria-label="Loading"></span></div></div>
</div>
</div>
</div>
</form>
</div>
<ul class="breadcrumb repo-breadcrumb">
<li class="breadcrumb-item">
<a href="/gitlab/prunonos/com490-lab-course/-/tree/master">com490-lab-course
</a></li>
<li class="breadcrumb-item">
<a href="/gitlab/prunonos/com490-lab-course/-/tree/master/week1">week1</a>
</li>
<li class="breadcrumb-item">
<a href="/gitlab/prunonos/com490-lab-course/-/blob/master/week1/exercises-1_python-essentials.py"><strong>exercises-1_python-essentials.py</strong>
</a></li>
</ul>
</div>
<div class="tree-controls gl-children-ml-sm-3"><a class="gl-button btn btn-default shortcuts-find-file" rel="nofollow" href="/gitlab/prunonos/com490-lab-course/-/find_file/master">Find file
</a><a class="gl-button btn btn-default js-blob-blame-link" href="/gitlab/prunonos/com490-lab-course/-/blame/master/week1/exercises-1_python-essentials.py">Blame</a><a class="gl-button btn btn-default" href="/gitlab/prunonos/com490-lab-course/-/commits/master/week1/exercises-1_python-essentials.py">History</a><a class="gl-button btn btn-default js-data-file-blob-permalink-url" href="/gitlab/prunonos/com490-lab-course/-/blob/9fbc8c76390458e268685d4cebed35f5381e3095/week1/exercises-1_python-essentials.py">Permalink</a></div>
</div>

<div class="info-well d-none d-sm-block">
<div class="well-segment">
<ul class="blob-commit-info">
<li class="commit flex-row js-toggle-container" id="commit-9fbc8c76">
<div class="avatar-cell d-none d-sm-block">
<a href="/gitlab/prunonos"><img alt="Guillem Pruñonosa Soler&#39;s avatar" src="https://secure.gravatar.com/avatar/4c73ce167ffa00867a43a4450e07ceb5?s=80&amp;d=identicon" class="avatar s40 d-none d-sm-inline-block" title="Guillem Pruñonosa Soler" /></a>
</div>
<div class="commit-detail flex-list">
<div class="commit-content" data-qa-selector="commit_content">
<a class="commit-row-message item-title js-onboarding-commit-item " href="/gitlab/prunonos/com490-lab-course/-/commit/9fbc8c76390458e268685d4cebed35f5381e3095">ex1 (not fin)</a>
<span class="commit-row-message d-inline d-sm-none">
&middot;
9fbc8c76
</span>
<div class="committer">
<a class="commit-author-link js-user-link" data-user-id="67" href="/gitlab/prunonos">Guillem Pruñonosa Soler</a> authored <time class="js-timeago" title="Mar 2, 2022 11:27am" datetime="2022-03-02T11:27:25Z" data-toggle="tooltip" data-placement="bottom" data-container="body">Mar 02, 2022</time>
</div>

</div>
<div class="commit-actions flex-row">

<a class="ci-status-link ci-status-icon-success d-inline-flex " title="Pipeline: passed" data-toggle="tooltip" data-placement="left" data-container="body" href="/gitlab/prunonos/com490-lab-course/-/commit/9fbc8c76390458e268685d4cebed35f5381e3095/pipelines?ref=master"><svg class="s24" data-testid="status_success-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#status_success"></use></svg></a>
<div class="js-commit-pipeline-status" data-endpoint="/gitlab/prunonos/com490-lab-course/-/commit/9fbc8c76390458e268685d4cebed35f5381e3095/pipelines?ref=master"></div>
<div class="commit-sha-group btn-group d-none d-sm-flex">
<div class="label label-monospace monospace">
9fbc8c76
</div>
<button class="btn gl-button btn btn-default btn-icon" data-toggle="tooltip" data-placement="bottom" data-container="body" data-title="Copy commit SHA" data-class="gl-button btn btn-default btn-icon" data-clipboard-text="9fbc8c76390458e268685d4cebed35f5381e3095" type="button" title="Copy commit SHA" aria-label="Copy commit SHA"><svg class="s16 gl-icon" data-testid="copy-to-clipboard-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#copy-to-clipboard"></use></svg></button>

</div>
</div>
</div>
</li>

</ul>
</div>


</div>
<div class="blob-content-holder" id="blob-content-holder">
<article class="file-holder">
<div class="js-file-title file-title-flex-parent">
<div class="file-header-content">
<svg class="s16" data-testid="doc-text-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#doc-text"></use></svg>
<strong class="file-title-name gl-word-break-all" data-qa-selector="file_name_content">
exercises-1_python-essentials.py
</strong>
<button class="btn gl-button btn btn-default-tertiary btn-icon btn-sm" data-toggle="tooltip" data-placement="bottom" data-container="body" data-class="gl-button btn btn-default-tertiary btn-icon btn-sm" data-title="Copy file path" data-clipboard-text="{&quot;text&quot;:&quot;week1/exercises-1_python-essentials.py&quot;,&quot;gfm&quot;:&quot;`week1/exercises-1_python-essentials.py`&quot;}" type="button" title="Copy file path" aria-label="Copy file path"><svg class="s16 gl-icon" data-testid="copy-to-clipboard-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#copy-to-clipboard"></use></svg></button>
<small class="mr-1">
10.5 KB
</small>
</div>

<div class="file-actions gl-display-flex gl-align-items-center gl-flex-wrap gl-md-justify-content-end"><a class="btn gl-button btn-confirm js-edit-blob gl-ml-3 " data-track-action="click_edit" data-track-label="edit" href="/gitlab/prunonos/com490-lab-course/-/edit/master/week1/exercises-1_python-essentials.py">Edit</a><a class="btn gl-button btn-confirm ide-edit-button gl-ml-3 btn-inverted" data-track-action="click_edit_ide" data-track-label="web_ide" data-track-property="secondary" href="/gitlab/-/ide/project/prunonos/com490-lab-course/edit/master/-/week1/exercises-1_python-essentials.py">Web IDE</a><div class="btn-group gl-ml-3" role="group">

<button name="button" type="submit" class="btn gl-button btn-default btn-default" data-target="#modal-upload-blob" data-toggle="modal">Replace</button>
<button name="button" type="submit" class="btn gl-button btn-default btn-default" data-target="#modal-remove-blob" data-toggle="modal">Delete</button>
</div><div class="btn-group gl-ml-3" role="group">
<span class="btn-group has-tooltip js-copy-blob-source-btn-tooltip"><button class="btn btn gl-button btn-default btn-icon js-copy-blob-source-btn" data-class="btn gl-button btn-default btn-icon js-copy-blob-source-btn" data-hide-tooltip="true" data-clipboard-target=".blob-content[data-blob-id=&#39;88b6797958f5e38729f474ff5acad79aef575ac3&#39;] &gt; pre" type="button" title="Copy" aria-label="Copy"><svg class="s16 gl-icon" data-testid="copy-to-clipboard-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#copy-to-clipboard"></use></svg></button></span>
<a class="btn gl-button btn-default btn-icon has-tooltip" target="_blank" rel="noopener noreferrer" aria-label="Open raw" title="Open raw" data-container="body" href="/gitlab/prunonos/com490-lab-course/-/raw/master/week1/exercises-1_python-essentials.py"><svg class="s16" data-testid="doc-code-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#doc-code"></use></svg></a>
<a download="week1/exercises-1_python-essentials.py" class="btn gl-button btn-default btn-icon has-tooltip" target="_blank" rel="noopener noreferrer" aria-label="Download" title="Download" data-container="body" href="/gitlab/prunonos/com490-lab-course/-/raw/master/week1/exercises-1_python-essentials.py?inline=false"><svg class="s16" data-testid="download-icon"><use href="/gitlab/assets/icons-74e006cef5a76d001c81e4dda159833de67bd6dbd16e42db899bbe43f2a76cf2.svg#download"></use></svg></a>

</div></div>
</div>
<div class="js-file-fork-suggestion-section file-fork-suggestion hidden">
<span class="file-fork-suggestion-note">You can’t <span class="js-file-fork-suggestion-section-action">edit</span> files directly in this project. Fork this project and submit a merge request with your changes.</span>
<a class="js-fork-suggestion-button gl-button btn btn-grouped btn-confirm-secondary" rel="nofollow" data-method="post" href="/gitlab/prunonos/com490-lab-course/-/blob/master/week1/exercises-1_python-essentials.py">Fork</a>
<button class="js-cancel-fork-suggestion-button gl-button btn btn-grouped" type="button">
Cancel
</button>
</div>



<div class="blob-viewer" data-path="week1/exercises-1_python-essentials.py" data-type="simple" data-url="/gitlab/prunonos/com490-lab-course/-/blob/master/week1/exercises-1_python-essentials.py?format=json&amp;viewer=simple">
<div class="text-center gl-mt-4 gl-mb-3">
<span class="gl-spinner gl-spinner-orange gl-spinner-md qa-spinner" aria-label="Loading"></span>
</div>

</div>


</article>
</div>

<div class="modal" id="modal-remove-blob">
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<h3 class="page-title">Delete exercises-1_python-essentials.py</h3>
<button aria-label="Close" class="close" data-dismiss="modal" type="button">
<span aria-hidden="true">&times;</span>
</button>
</div>
<div class="modal-body">
<form class="js-delete-blob-form js-quick-submit js-requires-input" action="/gitlab/prunonos/com490-lab-course/-/blob/master/week1/exercises-1_python-essentials.py" accept-charset="UTF-8" method="post"><input type="hidden" name="_method" value="delete" /><input type="hidden" name="authenticity_token" value="dozRw416GUQccs/pmDoANXYAH85m13HPAwVfuxQRQza7x0vDhhetTPi1pdVTap/ifM+8KwuNFxRb3PhReN3aGQ==" /><div class="form-group row commit_message-group">
<label class="col-form-label col-sm-2" for="commit_message-baca53657d74587797e7cd1841164761">Commit message
</label><div class="col-sm-10">
<div class="commit-message-container">
<div class="max-width-marker"></div>
<textarea name="commit_message" id="commit_message-baca53657d74587797e7cd1841164761" class="form-control gl-form-input js-commit-message" placeholder="Delete exercises-1_python-essentials.py" data-qa-selector="commit_message_field" required="required" rows="3">
Delete exercises-1_python-essentials.py</textarea>
</div>
</div>
</div>

<div class="form-group row branch">
<label class="col-form-label col-sm-2" for="branch_name">Target Branch</label>
<div class="col-sm-10">
<input type="text" name="branch_name" id="branch_name" value="master" required="required" class="form-control gl-form-input js-branch-name ref-name" />
<div class="js-create-merge-request-container">
<div class="form-check gl-mt-3">
<input type="checkbox" name="create_merge_request" id="create_merge_request-f936a41f90d4bca2771d3a043b9452c6" value="1" class="js-create-merge-request form-check-input" checked="checked" />
<label class="form-check-label" for="create_merge_request-f936a41f90d4bca2771d3a043b9452c6">Start a <strong>new merge request</strong> with these changes
</label></div>

</div>
</div>
</div>
<input type="hidden" name="original_branch" id="original_branch" value="master" class="js-original-branch" />

<div class="form-group row">
<div class="offset-sm-2 col-sm-10">
<button name="button" type="submit" class="btn gl-button btn-danger btn-remove-file">Delete file</button>
<a class="btn gl-button btn-cancel" data-dismiss="modal" href="#">Cancel</a>
</div>
</div>
</form></div>
</div>
</div>
</div>

<div class="modal" id="modal-upload-blob">
<div class="modal-dialog modal-lg">
<div class="modal-content">
<div class="modal-header">
<h3 class="page-title">Replace exercises-1_python-essentials.py</h3>
<button aria-label="Close" class="close" data-dismiss="modal" type="button">
<span aria-hidden="true">&times;</span>
</button>
</div>
<div class="modal-body">
<form class="js-quick-submit js-upload-blob-form" data-method="put" action="/gitlab/prunonos/com490-lab-course/-/update/master/week1/exercises-1_python-essentials.py" accept-charset="UTF-8" method="post"><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="/90j3asrLbGDpRI2JctTB3CcE6En5LlLl2j3HrmTEIsylrndoEaZuWdieArum8zQelOwREq+35DPsVD01V+JpA==" /><div class="dropzone">
<div class="dropzone-previews blob-upload-dropzone-previews">
<p class="dz-message light">
Attach a file by drag &amp; drop or <a class="markdown-selector" href="#">click to upload</a>
</p>
</div>
</div>
<br>
<div class="dropzone-alerts gl-alert gl-alert-danger gl-mb-5 data" style="display:none"></div>
<div class="form-group row commit_message-group">
<label class="col-form-label col-sm-2" for="commit_message-a6ed57bcbb88409aae8676a41c57b6a0">Commit message
</label><div class="col-sm-10">
<div class="commit-message-container">
<div class="max-width-marker"></div>
<textarea name="commit_message" id="commit_message-a6ed57bcbb88409aae8676a41c57b6a0" class="form-control gl-form-input js-commit-message" placeholder="Replace exercises-1_python-essentials.py" data-qa-selector="commit_message_field" required="required" rows="3">
Replace exercises-1_python-essentials.py</textarea>
</div>
</div>
</div>

<div class="form-group row branch">
<label class="col-form-label col-sm-2" for="branch_name">Target Branch</label>
<div class="col-sm-10">
<input type="text" name="branch_name" id="branch_name" value="master" required="required" class="form-control gl-form-input js-branch-name ref-name" />
<div class="js-create-merge-request-container">
<div class="form-check gl-mt-3">
<input type="checkbox" name="create_merge_request" id="create_merge_request-cd5ef6d1f71d90ac9544d6bdfb233416" value="1" class="js-create-merge-request form-check-input" checked="checked" />
<label class="form-check-label" for="create_merge_request-cd5ef6d1f71d90ac9544d6bdfb233416">Start a <strong>new merge request</strong> with these changes
</label></div>

</div>
</div>
</div>
<input type="hidden" name="original_branch" id="original_branch" value="master" class="js-original-branch" />

<div class="form-actions">
<button name="button" type="button" class="btn gl-button btn-confirm btn-upload-file" id="submit-all"><div class="gl-spinner gl-mr-2 js-loading-icon hidden"></div>
Replace file
</button><a class="btn gl-button btn-default btn-cancel" data-dismiss="modal" href="#">Cancel</a>

</div>
</form></div>
</div>
</div>
</div>

</div>

<script>
//<![CDATA[
  window.gl = window.gl || {};
  window.gl.webIDEPath = '/gitlab/-/ide/project/prunonos/com490-lab-course/edit/master/-/week1/exercises-1_python-essentials.py'


//]]>
</script>

</main>
</div>


</div>
</div>
<div class="top-nav-responsive layout-page content-wrapper-margin">
<div data-view-model="{&quot;primary&quot;:[{&quot;id&quot;:&quot;project&quot;,&quot;title&quot;:&quot;Projects&quot;,&quot;active&quot;:true,&quot;icon&quot;:&quot;project&quot;,&quot;href&quot;:&quot;&quot;,&quot;view&quot;:&quot;projects&quot;,&quot;css_class&quot;:&quot;qa-projects-dropdown&quot;,&quot;data&quot;:{&quot;track_label&quot;:&quot;projects_dropdown&quot;,&quot;track_action&quot;:&quot;click_dropdown&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;groups&quot;,&quot;title&quot;:&quot;Groups&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;group&quot;,&quot;href&quot;:&quot;&quot;,&quot;view&quot;:&quot;groups&quot;,&quot;css_class&quot;:&quot;qa-groups-dropdown&quot;,&quot;data&quot;:{&quot;track_label&quot;:&quot;groups_dropdown&quot;,&quot;track_action&quot;:&quot;click_dropdown&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;milestones&quot;,&quot;title&quot;:&quot;Milestones&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;clock&quot;,&quot;href&quot;:&quot;/gitlab/dashboard/milestones&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;milestones_link&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;snippets&quot;,&quot;title&quot;:&quot;Snippets&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;snippet&quot;,&quot;href&quot;:&quot;/gitlab/dashboard/snippets&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;snippets_link&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;activity&quot;,&quot;title&quot;:&quot;Activity&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;history&quot;,&quot;href&quot;:&quot;/gitlab/dashboard/activity&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;activity_link&quot;},&quot;emoji&quot;:null}],&quot;secondary&quot;:[],&quot;views&quot;:{&quot;projects&quot;:{&quot;namespace&quot;:&quot;projects&quot;,&quot;currentUserName&quot;:&quot;prunonos&quot;,&quot;currentItem&quot;:{&quot;id&quot;:105,&quot;name&quot;:&quot;com490-lab-course&quot;,&quot;namespace&quot;:&quot;Guillem Pruñonosa Soler / com490-lab-course&quot;,&quot;webUrl&quot;:&quot;/gitlab/prunonos/com490-lab-course&quot;,&quot;avatarUrl&quot;:null},&quot;linksPrimary&quot;:[{&quot;id&quot;:&quot;your&quot;,&quot;title&quot;:&quot;Your projects&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/dashboard/projects&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Your projects&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;starred&quot;,&quot;title&quot;:&quot;Starred projects&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/dashboard/projects/starred&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Starred projects&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;explore&quot;,&quot;title&quot;:&quot;Explore projects&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/explore&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Explore projects&quot;},&quot;emoji&quot;:null}],&quot;linksSecondary&quot;:[{&quot;id&quot;:&quot;create&quot;,&quot;title&quot;:&quot;Create new project&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/projects/new&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Create new project&quot;},&quot;emoji&quot;:null}]},&quot;groups&quot;:{&quot;namespace&quot;:&quot;groups&quot;,&quot;currentUserName&quot;:&quot;prunonos&quot;,&quot;currentItem&quot;:{},&quot;linksPrimary&quot;:[{&quot;id&quot;:&quot;your&quot;,&quot;title&quot;:&quot;Your groups&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/dashboard/groups&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Your groups&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;explore&quot;,&quot;title&quot;:&quot;Explore groups&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/explore/groups&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Explore groups&quot;},&quot;emoji&quot;:null}],&quot;linksSecondary&quot;:[{&quot;id&quot;:&quot;create&quot;,&quot;title&quot;:&quot;Create group&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/groups/new&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Create group&quot;},&quot;emoji&quot;:null}]},&quot;new&quot;:{&quot;title&quot;:&quot;New...&quot;,&quot;menu_sections&quot;:[{&quot;title&quot;:&quot;This project&quot;,&quot;menu_items&quot;:[{&quot;id&quot;:&quot;new_issue&quot;,&quot;title&quot;:&quot;New issue&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/prunonos/com490-lab-course/-/issues/new&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;track_action&quot;:&quot;click_link_new_issue&quot;,&quot;track_label&quot;:&quot;plus_menu_dropdown&quot;,&quot;qa_selector&quot;:&quot;new_issue_link&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;new_mr&quot;,&quot;title&quot;:&quot;New merge request&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/prunonos/com490-lab-course/-/merge_requests/new&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;track_action&quot;:&quot;click_link_new_mr&quot;,&quot;track_label&quot;:&quot;plus_menu_dropdown&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;new_snippet&quot;,&quot;title&quot;:&quot;New snippet&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/prunonos/com490-lab-course/-/snippets/new&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;track_action&quot;:&quot;click_link_new_snippet_project&quot;,&quot;track_label&quot;:&quot;plus_menu_dropdown&quot;},&quot;emoji&quot;:null}]},{&quot;title&quot;:&quot;GitLab&quot;,&quot;menu_items&quot;:[{&quot;id&quot;:&quot;general_new_project&quot;,&quot;title&quot;:&quot;New project/repository&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/projects/new&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;track_action&quot;:&quot;click_link_new_project&quot;,&quot;track_label&quot;:&quot;plus_menu_dropdown&quot;,&quot;qa_selector&quot;:&quot;global_new_project_link&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;general_new_group&quot;,&quot;title&quot;:&quot;New group&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/groups/new&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;track_action&quot;:&quot;click_link_new_group&quot;,&quot;track_label&quot;:&quot;plus_menu_dropdown&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;general_new_snippet&quot;,&quot;title&quot;:&quot;New snippet&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/-/snippets/new&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;track_action&quot;:&quot;click_link_new_snippet_parent&quot;,&quot;track_label&quot;:&quot;plus_menu_dropdown&quot;,&quot;qa_selector&quot;:&quot;global_new_snippet_link&quot;},&quot;emoji&quot;:null}]}]},&quot;search&quot;:{&quot;id&quot;:&quot;search&quot;,&quot;title&quot;:&quot;Search&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;search&quot;,&quot;href&quot;:&quot;/gitlab/search?project_id=105&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:null,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Search&quot;},&quot;emoji&quot;:null}},&quot;shortcuts&quot;:[{&quot;id&quot;:&quot;project-shortcut&quot;,&quot;title&quot;:&quot;Projects&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/dashboard/projects&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-projects&quot;,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Projects&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;groups-shortcut&quot;,&quot;title&quot;:&quot;Groups&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/dashboard/groups&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-groups&quot;,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Groups&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;milestones-shortcut&quot;,&quot;title&quot;:&quot;Milestones&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/dashboard/milestones&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-milestones&quot;,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Milestones&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;snippets-shortcut&quot;,&quot;title&quot;:&quot;Snippets&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/dashboard/snippets&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-snippets&quot;,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Snippets&quot;},&quot;emoji&quot;:null},{&quot;id&quot;:&quot;activity-shortcut&quot;,&quot;title&quot;:&quot;Activity&quot;,&quot;active&quot;:false,&quot;icon&quot;:&quot;&quot;,&quot;href&quot;:&quot;/gitlab/dashboard/activity&quot;,&quot;view&quot;:&quot;&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-activity&quot;,&quot;data&quot;:{&quot;qa_selector&quot;:&quot;menu_item_link&quot;,&quot;qa_title&quot;:&quot;Activity&quot;},&quot;emoji&quot;:null}],&quot;activeTitle&quot;:&quot;Menu&quot;}" id="js-top-nav-responsive"></div>
</div>



<script>
//<![CDATA[
if ('loading' in HTMLImageElement.prototype) {
  document.querySelectorAll('img.lazy').forEach(img => {
    img.loading = 'lazy';
    let imgUrl = img.dataset.src;
    // Only adding width + height for avatars for now
    if (imgUrl.indexOf('/avatar/') > -1 && imgUrl.indexOf('?') === -1) {
      const targetWidth = img.getAttribute('width') || img.width;
      imgUrl += `?width=${targetWidth}`;
    }
    img.src = imgUrl;
    img.removeAttribute('data-src');
    img.classList.remove('lazy');
    img.classList.add('js-lazy-loaded', 'qa-js-lazy-loaded');
  });
}

//]]>
</script>

</body>
</html>

