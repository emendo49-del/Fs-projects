import matplotlib.pyplot as plt
import polars as pl
import numpy as np

def dashPanel():
    # Load and filter data
    df = pl.read_parquet("08102025Endurance1_FirstHalf.parquet")
    df = df.filter(pl.col("VDM_GPS_VALID1") != 0)

    # Creating a layout, changing 2,2 will increase size, (2*2 = 4 spaces and so on )
    fig, axs = plt.subplots(2,2, figsize= (12,16))
    fig.suptitle("Car Data", fontsize = 16)

    ax1 = axs[0,1]
    ax1.plot(df["ACC_POWER_SOC"], label="SOC (%)", color="green")
    ax1.plot(df["ACC_POWER_PACK_VOLTAGE"], label="Pack Voltage (V)", color="blue")
    ax1.set_ylabel("SOC / Voltage")
    ax1.set_xlabel("Sample Index")
    ax1.legend()
    ax1.grid(True)

    ax2 = axs[0,0]
    ax2.plot(df["SME_TEMP_BusCurrent"], label="Motor Current (A)", color="red")
    ax2.plot(df["SME_TRQSPD_Torque"], label="Torque (Nm)", color="orange")
    ax2.plot(df["VDM_GPS_SPEED"], label="Speed (mph)", color="green")
    ax2.set_ylabel("Current / Torque / Speed")
    ax2.set_xlabel("Sample Index")
    ax2.legend()
    ax2.grid(True)

    ax3 = axs[1,0]
    ax3.plot(df["ETC_STATUS_BRAKE_SENSE_VOLTAGE"], label="Brake Input (V)", color="crimson")
    ax3.plot(df["VDM_GPS_SPEED"], color="blue", label="Speed (mph)")
    ax3.set_ylabel("Brake / RTDS")
    ax3.set_xlabel("Sample Index")
    ax3.legend()
    ax3.grid(True)   

    ax4 = axs[1,1]
    sc = ax4.scatter(df["VDM_GPS_Longitude"], df["VDM_GPS_Latitude"], c = df["VDM_GPS_SPEED"], cmap="plasma", s=5)
    ax4.set_xlabel("Longitude")
    ax4.set_ylabel("Latitude")
    ax4.set_title("GPS Track Colored by Speed")
    fig.colorbar(sc, ax=ax4, label="Speed (mph)")
    ax4.grid(True)
    
    
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

if __name__ == "__main__":
    dashPanel()

