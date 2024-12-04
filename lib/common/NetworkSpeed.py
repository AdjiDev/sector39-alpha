from .InstallModule import InstallModule

try:
    import speedtest
except ImportError:
    InstallModule("speedtest-cli")
from .Cols import warna
from .delay import TimeDelay


def NetworkSpeedTest():
    ingfo = f"[   {warna.y}INFO{warna.reset}   ]"
    ok = f"[    {warna.g}OK{warna.reset}    ]"
    fatal = f"[   {warna.r}FATAL{warna.reset}]"
    try:
        st = speedtest.Speedtest()
        tuma = TimeDelay()
        adjisan = next(tuma)
        print(f"{adjisan}{ingfo} Finding best network server . . .")
        try:
            st.get_best_server()
        except Exception as server_error:
            adjisan = next(tuma)
            print(f"{adjisan}{fatal} Failed to find the best server: {server_error}")
            adjisan = next(tuma)
            print(f"{adjisan}{ingfo} Using default server.")
        adjisan = next(tuma)
        print(f"{adjisan}{ingfo} Testing download speed . . .")
        donlot = st.download() / 1_000_000
        adjisan = next(tuma)
        print(f"{adjisan}{ingfo} Testing upload speed . . .")
        aplot = st.upload() / 1_000_000
        adjisan = next(tuma)
        print(f"{adjisan}{ingfo} Pinging the results . . .")
        ping = st.results.ping

        print(f"=============== {warna.g}SPEEDTEST RESULT{warna.reset} ===============")
        print(
            f"{warna.y}Download{warna.reset}   : {warna.g}{donlot:.2f}{warna.reset} Mbps"
        )
        print(
            f"{warna.y}Upload{warna.reset}     : {warna.g}{aplot:.2f}{warna.reset} Mbps"
        )
        print(f"{warna.y}Ping{warna.reset}       : {warna.g}{ping:.2f}{warna.reset} ms")

    except speedtest.ConfigRetrievalError as config_error:
        adjisan = next(tuma)
        print(f"{adjisan}{fatal} Failed to retrieve speedtest configuration: {config_error}")
        return False
    except speedtest.HTTP_ERRORS as http_error:
        adjisan = next(tuma)
        print(f"{adjisan}{fatal} HTTP error occurred: {http_error}")
        return False
    except Exception as e:
        adjisan = next(tuma)
        print(f"{adjisan}{fatal} {e}")
        return False
    except KeyboardInterrupt:
        adjisan = next(tuma)
        print(f"{adjisan}{fatal} Operation canceled by user.")
        return False

    return True

