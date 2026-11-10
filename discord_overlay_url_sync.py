import obspython as obs

source_name = "Discord-Overlay"
target_name = "Discord-VC"
last_url = None


def script_description():
    return (
        "Discord-Overlayが変更したブラウザソースのURLを、別のブラウザソースに同期します。\n"
        "各ソースのカスタムCSSは変更しません。"
    )


def script_defaults(settings):
    obs.obs_data_set_default_string(settings, "source_name", "Discord-Overlay")
    obs.obs_data_set_default_string(settings, "target_name", "Discord-VC")


def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_text(props, "source_name", "同期元のブラウザソース名", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(props, "target_name", "同期先のブラウザソース名", obs.OBS_TEXT_DEFAULT)
    return props


def script_update(settings):
    global source_name, target_name, last_url
    source_name = obs.obs_data_get_string(settings, "source_name").strip()
    target_name = obs.obs_data_get_string(settings, "target_name").strip()
    last_url = None


def sync_url():
    global last_url
    if not source_name or not target_name or source_name == target_name:
        return

    src = obs.obs_get_source_by_name(source_name)
    if src is None:
        return
    try:
        if obs.obs_source_get_unversioned_id(src) != "browser_source":
            return
        settings = obs.obs_source_get_settings(src)
        try:
            url = obs.obs_data_get_string(settings, "url")
        finally:
            obs.obs_data_release(settings)
    finally:
        obs.obs_source_release(src)

    if not url or url == last_url:
        return

    dst = obs.obs_get_source_by_name(target_name)
    if dst is None:
        return
    try:
        if obs.obs_source_get_unversioned_id(dst) != "browser_source":
            return
        dst_settings = obs.obs_source_get_settings(dst)
        try:
            if obs.obs_data_get_string(dst_settings, "url") != url:
                obs.obs_data_set_string(dst_settings, "url", url)
                obs.obs_source_update(dst, dst_settings)
            last_url = url
        finally:
            obs.obs_data_release(dst_settings)
    finally:
        obs.obs_source_release(dst)


def script_load(settings):
    obs.timer_add(sync_url, 500)


def script_unload():
    obs.timer_remove(sync_url)
