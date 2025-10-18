import matplotlib.pyplot as plt
import polars as pl
import numpy as np

def dashPanel(vehicle_mass= 1000, air_density = 1.225):
    # Load and filter data
    df = pl.read_parquet("08102025Endurance1_FirstHalf.parquet")
    df = df.filter(pl.col("VDM_GPS_VALID1") != 0)

    # Creating a layout, changing 2,2 will increase size, (2*2 = 4 spaces and so on )
    fig, axs = plt.subplots(2,2, figsize= (14,16))
    fig.suptitle("Car Data with Estimated Drag (CdA)", fontsize = 16)

    speed_mps = df["VDM_GPS_SPEED"].to_numpy()* 0.44704
    acceleration = df["VDM_X_AXIS_ACCELERATION"].to_numpy()
    torque = df["SME_TRQSPD_Torque"].to_numpy()

    # Traction force, estimated wheel radius
    wheel_radius = 0.3
    traction_force = torque / wheel_radius

    # Drag force calculation
    net_force = traction_force - vehicle_mass * acceleration
    speed_sq = np.where(speed_mps**2 > 0, speed_mps**2, 1e-3)

    # Estimated CdA
    CdA = 2 * net_force / (air_density * speed_sq)

    ax1 = axs[0,0]
    ax1.plot(df["VDM_GPS_SPEED"], label="Speed (mph)", color="green")
    ax1.plot(acceleration, label = "x acceleration (m/s^2)")
    ax1.legend()
    ax1.grid(True)

    ax2 = axs[0,1]
    ax2.plot(torque, label="Motor Torque (Nm)", color="orange")
    ax2.plot(traction_force, label="Traction Force (N)", color="red")
    # ax2.set_ylabel("Current / Torque / Speed")
    # ax2.set_xlabel("Sample Index")
    ax2.legend()
    ax2.grid(True)

    ax3 = axs[1,0]
    ax3.plot(CdA, label="Estimated CdA", color="purple")
    ax3.set_ylabel("Cd × A (m²)")
    # ax3.set_xlabel("Sample Index")
    ax3.legend()
    ax3.grid(True)   

    # ax4 = axs[1,1]
    # sc = ax4.scatter(df["VDM_GPS_Longitude"], df["VDM_GPS_Latitude"], c = df["VDM_GPS_SPEED"], cmap="plasma", s=5)
    # ax4.set_xlabel("Longitude")
    # ax4.set_ylabel("Latitude")
    # ax4.set_title("GPS Track Colored by Speed")
    # fig.colorbar(sc, ax=ax4, label="Speed (mph)")
    # ax4.grid(True)
    
    
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

if __name__ == "__main__":
    dashPanel(vehicle_mass=1200)

