import matplotlib.pyplot as plt
import polars as pl
import numpy as np

def dashPanel():
    # Load and filter data
    df = pl.read_parquet("08102025Endurance1_FirstHalf.parquet")
    df = df.filter(pl.col("VDM_GPS_VALID1") != 0)

    # Creating a layout, changing 2,2 will increase size, (2*2 = 4 spaces and so on )
    fig, axs = plt.subplots(2,2, figsize= (10,8))
    fig.suptitle("Car Data", fontsize = 16)

    ax1 = axs[0,1]
    ax1.plot(df["VDM_GPS_SPEED"], label = "Speed (mph)")
    ax1.plot(df["ETC_STATUS_RTDS"], label = "RTDS")
    ax1.set_ylabel("Speed (mph)")
    ax1.legend()
    ax1.grid(True)

    ax2 = axs[0,0]
    ax2.plot(df["VDM_GPS_Latitude"], df["VDM_GPS_Longitude"], label = "road", color = "tab:green")
    ax2.set_ylabel("Positioning")
    ax2.legend()
    ax2.grid(True)

    ax3 = axs[1,0]
    ax3.plot(df["ACC_POWER_SOC"], label = "battery",color = "tab:orange")
    ax3.set_ylabel("Power Supply")
    ax3.legend()
    ax3.grid(True)

    ax4 = axs[1,1]
    ax4.plot(df["ETC_STATUS_BRAKE_SENSE_VOLTAGE"], label = "brakes", color = "tab:red")
    ax4.set_ylabel("Brake input")
    ax4.legend()
    ax4.grid(True)
    
    
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

if __name__ == "__main__":
    dashPanel()

