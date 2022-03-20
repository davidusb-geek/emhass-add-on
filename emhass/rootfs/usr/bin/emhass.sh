#!/usr/bin/with-contenv bashio
# ==============================================================================
# Home Assistant Community Add-on: EMHASS
#
# ==============================================================================


# ==============================================================================
# RUN LOGIC
# ------------------------------------------------------------------------------
main() {
    local sleep

    bashio::log.trace "${FUNCNAME[0]}"

    sleep=$(bashio::config 'seconds_to_publish_data')
    bashio::log.info "Seconds between each publish is set to: ${sleep}"

    while true; do
        #emhass --action 'publish-data' --config '/data/config_emhass.yaml'
        bashio::log.info "Publishing data"
        sleep "${sleep}"
    done
}
main "$@"
