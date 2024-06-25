from typing import Optional, List, Union
from pydantic import BaseModel, EmailStr
from datetime import datetime, date, time, timedelta

import re

# user schemas
class UserBase(BaseModel):
    FirstName: str
    LastName: str
    Email: EmailStr
    Phone: Optional[str] = None
    Role: str
    BirthDate: Optional[date] = None
    Address: Optional[str] = None
class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    Password: Optional[str] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    Email: Optional[str] = None
    Phone: Optional[str] = None
    Role: Optional[str] = None
    BirthDate: Optional[date] = None
    Address: Optional[str] = None

class UserSetPassword(BaseModel):
    token: str
    new_password: str
  

class User(UserBase):
    UserID: int

    class Config:
        from_attributes = True

class UserRegistration(BaseModel):
    Email: str
    FirstName: str
    LastName: str
    Role: str
    Password: str


class UserLogin(BaseModel):
    Email: str
    Password: str
    


class UserVerification(BaseModel):
    Email:str
    Code: str

class UserResetPassword(BaseModel):
    Email: EmailStr
    new_password : str


class UserforCentra(BaseModel):
    FirstName: str
    LastName: str
    Email: str

# User (Admin)
class AdminBase(BaseModel):
    PIC_name: str
    email: EmailStr
    phone: Optional[str] = None

class AdminCreate(AdminBase):
    pass

class AdminUpdate(BaseModel):
    PIC_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

class Admin(AdminBase):
    id: int  # Assuming an 'id' field is automatically generated by the database

    class Config:
        from_attributes = True  # This setting is crucial for compatibility with ORMs like SQLAlchemy

#CentraShipment
# class CentraShipmentBase(BaseModel):
#     ShippingMethod: str
#     AirwayBill: str
#     batch_ids: List[int] = []

# class CentraShipmentCreate(CentraShipmentBase):
#     pass

# class CentraShipment(CentraShipmentBase):
#     id: int

#     class Config:
#         orm_mode = True

# ProcessedLeaves schemas
class ProcessedLeavesBase(BaseModel):
    CentraID: Optional[int] = None
    Weight: Optional[float] = None
    DriedID: Optional[int] = None
    # DryingID: Optional[int] = None
    # FlouringID: Optional[int] = None
    # DriedDate: Optional[date] = None
    FlouredDate: date
    Shipped: Optional[bool] = False

class ProcessedLeaves_DriedDate(BaseModel):
    ProductID: int
    CentraID: Optional[int] = None
    Weight: Optional[int] = None
    DriedID: Optional[int] = None
    DriedDate: date 
    FlouredDate: date
    Shipped: Optional[bool] = False

# class ProcessedLeavesWithDriedDate(BaseModel):
#     ProductID: int
#     CentraID: int
#     Weight: float
#     FlouredDate: Optional[date]
#     Shipped: Optional[bool]
#     DriedDate: Optional[date]

#     class Config:
#         true_config = True


class ProcessedLeavesCreate(ProcessedLeavesBase):
    pass

class ProcessedLeavesRescale(BaseModel):
    Weight: float

class ProcessedLeavesShipped(BaseModel):
    Shipped: bool

class BatchShippedRequest(BaseModel):
    batch_ids: List[int]

   

class ProcessedLeaves(ProcessedLeavesBase):
    ProductID: int
    # creator_id: Optional[int]
    # shipments: Optional[List[CentraShipment]] = []

    class Config:
        orm_mode = True

# WetLeavesCollection schemas
class WetLeavesCollectionBase(BaseModel):
    # Define the base fields for your Pydantic model
    CentralID: int
    Date: date
    Time: time
    Weight: float
    Status: str
    Expired: Optional[bool] = False
    Dried: Optional [bool] = False
    # Duration: Optional[timedelta]
    # ExpirationTime: Optional[time] = None
    # ExpiredTime: time

class WetLeavesCollectionCreate(WetLeavesCollectionBase):
    pass

class WetLeavesCollectionUpdate(BaseModel):
    Date: Optional[date] = None
    Time: Optional[time] = None
    Weight: Optional[float] = None
    Status: Optional[str] = None
    Expired: Optional[bool] = False
    Dried: Optional [bool] = False
    
    # ExpiredTime: Optional[time] = None
    # ExpirationTime: Optional[time] = None

class WetLeavesCollection(WetLeavesCollectionBase):
    WetLeavesBatchID: int
    # creator_id: Optional[int]

    class Config:
        from_attributes = True


class ConversionRate(BaseModel):
    conversion_rate: float

# Centra Details
class CentraBase(BaseModel):
    Address: str

class CentraCreate(CentraBase):
    pass

class CentraDetails(CentraBase):
    CentralID: int

    class Config: 
        from_attributes = True

#userCentra

class UserCentraBase(BaseModel):
    CentraID: int
    userID: int
    Active: bool

class UserCentraCreate(UserCentraBase):
    pass

class UserCentraUpdate(BaseModel):
    CentraID: Optional[int] = None
    userID: Optional[int] = None
    Active: Optional[bool] = False

class UserCentra(UserCentraBase):
    id: int

    class Config:
        orm_mode = True

class UserforCentra(BaseModel):
    FirstName: str
    LastName: str
    Email: EmailStr

class UserCentraWithUser(BaseModel):
    usercentra: UserCentra
    user: UserforCentra

    class Config:
        orm_mode = True

# DryingMachine schemas
class DryingMachineBase(BaseModel):
    CentraID: int
    Capacity: str
    # Load: float
    Status: str
    Duration: Optional[timedelta]


class DryingMachineCreate(DryingMachineBase):
    pass

class DryingMachineUpdate(BaseModel):
    Capacity: Optional[str] = None
    Load: float

class DryingMachine(DryingMachineBase):
    MachineID: int
    # creator_id: Optional[int]

    class Config:
        orm_mode = True

# class MachineStatus(BaseModel):
#     status: str



# DryingActivity schemas
class DryingActivityBase(BaseModel):
    CentralID: int
    InUse: Optional[bool] = False
    Weight: float
    DryingMachineID: int
    EndTime: datetime

class DryingActivityCreate(BaseModel):
    Weight: float
    DryingMachineID: int
    EndTime: datetime
    InUse: Optional[bool] = False


class DryingActivityUpdate(BaseModel):
    DryingID: Optional[int] = None
    UserID: Optional[int] = None
    CentralID: Optional[int] = None
    InUse: Optional[bool] = False
    Weight: Optional[float] = None
    DryingMachineID: Optional[str] = None
    EndTime: Optional[datetime] = None

class DryingActivity(DryingActivityBase):
    DryingID: int
    # creator_id: Optional[int]

    class Config:
        from_attributes = True

#driedleaves
class DriedLeavesBase(BaseModel):
    id:int
    CentraID: int
    Weight: float
    DriedDate: date
    Floured: Optional[bool] = False
    InMachine: Optional[bool] = False

class DriedLeavesCreate(BaseModel):
    CentraID: int
    Weight: float
    DriedDate: str
    Floured: Optional[bool] = False
    InMachine: Optional[bool] = False

class DriedLeavesUpdate(BaseModel):
    CentraID: Optional[int] = None
    Weight: Optional[float] = None
    DriedDate: Optional[date] = None
    Floured: Optional[bool] = None
    InMachine: Optional[bool] = False

class DriedLeaves(DriedLeavesBase):
    id: int

    class Config:
        from_attributes = True

class DriedLeavesUpdateInMachine(BaseModel):
    in_machine: bool

# FlouringMachine schemas
class FlouringMachineBase(BaseModel):
    CentraID: int
    Capacity: str
    Load: float
    Status: str
    Duration: Optional[timedelta]

class FlouringMachineCreate(FlouringMachineBase):
    pass

class FlouringMachineUpdate(BaseModel):
    Capacity: Optional[str] = None
    Load: float

class FlouringMachine(FlouringMachineBase):
    MachineID: int
    # creator_id: Optional[int]

    class Config:
        from_attributes = True

class StatusUpdateRequest(BaseModel):
    machine_id :int
    status: str



# FlouringActivity schemas
class FlouringActivityBase(BaseModel):
    CentralID: Optional[int] = None
    EndTime: Optional[datetime]
    Weight: Optional[float] = None
    FlouringMachineID: Optional[int] = None
    InUse:Optional[bool] = False
    DriedDate: Optional[datetime]
    # DryingID: Optional[int] = None
    # Time: Optional[time] = None


class FlouringActivityCreate(FlouringActivityBase):
    pass


class FlouringActivityUpdate(BaseModel):
    FlouringID: Optional[int] = None
    UserID: Optional[int] = None
    CentralID: Optional[int] = None
    EndTime: Optional[datetime]
    DriedDate: Optional[datetime]
    InUse:Optional[bool] = False
    Weight: Optional[float] = None
    FlouringMachineID: Optional[int] = None
    # DryingID: Optional[str] = None
    # Time: Optional[time] = None

class FlouringActivity(FlouringActivityBase):
    FlouringID: int
    # creator_id: Optional[int]

    class Config:
        from_attributes = True

#stocks
class StockBase(BaseModel):
    product_id: int
    weight: float

class StockCreate(StockBase):
    pass

class StockUpdate(StockBase):
    pass

class Stock(StockBase):
    id: int
    location_id: Optional[int] = None

    class Config:
        from_attributes = True

# Centra schemas
# class CentraBase(BaseModel):
#     Address: str
#     FlouringSchedule: str

# class CentraCreate(CentraBase):
#     pass

class CentraUpdate(BaseModel):
    Address: Optional[str] = None
    # FlouringSchedule: Optional[str] = None

class Centra(CentraBase):
    CentralID: int

    class Config:
        from_attributes = True

#notifications
class NotificationBase(BaseModel):
    message: str
    centraid: int

class NotificationCreate(NotificationBase):
    pass

class Notification(NotificationBase):
    id: int
    # centraid: int
    timestamp: datetime
    read: bool

    class Config:
        orm_mode: True

Machine = Union[DryingMachine, FlouringMachine]


#expeditionnotif
class ExpeditionNotification(BaseModel):
    message: str
    centraid: int

class ExpeditionNotificationCreate(NotificationBase):
    # centraid: int
    pass

class ExpeditionNotification(NotificationBase):
    id: int
    # centraid: int
    timestamp: datetime
    read: bool

    class Config:
        orm_mode: True


#Expedition schemas

class ExpeditionBase(BaseModel):
    AirwayBill: str
    EstimatedArrival: datetime
    TotalPackages: int
    TotalWeight: float
    Status: str
    ExpeditionDate: datetime
    ExpeditionServiceDetails: str
    WarehouseID: int



class ExpeditionCreate(BaseModel):
    AirwayBill: str
    EstimatedArrival: datetime
    TotalPackages: int
    TotalWeight: float
    ExpeditionDate: datetime
    ExpeditionServiceDetails: str
    WarehouseID: int

class ExpeditionUpdate(BaseModel):
    AirwayBill: Optional[str] = None
    EstimatedArrival: Optional[datetime] = None
    TotalPackages: Optional[int] = None
    TotalWeight: Optional[float] = None
    Status:str
    ExpeditionDate: Optional[datetime] = None
    ExpeditionServiceDetails: Optional[str] = None
    warehouseid: int
    

class Expedition(ExpeditionBase):
    ExpeditionID: Optional[int] = None

    class Config:
        orm_mode = True
        # from_attributes = True  # Enable from_orm support

class Batch(BaseModel):
    BatchID: int
    Weight: float
    FlouredDate: datetime
    DriedDate: datetime

class ExpeditionWithBatches(BaseModel):
    expedition: Expedition
    batches: List[Batch]
    checkpoint_status: Optional[str]
    checkpoint_statusdate: Optional[datetime]

class StatusUpdate(BaseModel):
    awb: str
    status: str

class WarehouseIDUpdate(BaseModel):
    warehouse_id: int


#ExpeditionContent


class ExpeditionContentBase(BaseModel):
    ExpeditionID: int
    BatchIDs: List[int]
    # checkpointID: int

class ExpeditionContentCreate(ExpeditionContentBase):
    pass

class ExpeditionContentUpdate(BaseModel):
    ExpeditionID: Optional[int] = None
    BatchIDs: Optional[List[int]] = None
    # checkpointID: Optional[int] = None

class ExpeditionContent(BaseModel):
    id: int
    ExpeditionID: int
    BatchID: int

    class Config:
        orm_mode = True


#checkpointStatus
class CheckpointStatusBase(BaseModel):
    expeditionid: int
    status: str
    statusdate: datetime


# class CheckpointStatusALL(BaseModel):
#     id: int
#     expeditionid: int
#     status: str
#     statusdate: datetime

class CheckpointStatusCreate(CheckpointStatusBase):
    pass

class CheckpointStatusCreateAirway(BaseModel):
    status: str
    statusdate: Optional[datetime] = None  # This field represents the status date



class CheckpointStatus(CheckpointStatusBase):
    id: int

    class Config:
        orm_mode = True

# PackageReceipt schemas
class PackageReceiptBase(BaseModel):
    # xyzid: int
    ExpeditionID: int
    TotalWeight: float
    TimeAccepted: datetime
    Note: str
    Date: datetime

class PackageReceiptCreate(PackageReceiptBase):
    pass

class PackageReceiptUpdate(BaseModel):
    # xyzid: Optional[int] = None
    ExpeditionID: Optional[int] = None
    TotalWeight: Optional[float] = None
    TimeAccepted: Optional[datetime] = None
    Note: Optional[str] = None
    Date: Optional[datetime] = None

class PackageReceipt(PackageReceiptBase):
    ReceiptID: int

    class Config:
        from_attributes = True


class PickupCreateAirway(BaseModel):
    warehouseid: int
    pickup_time: time

class PickupBase(BaseModel):
    expeditionID: int
    warehouseid: int
    pickup_time: time


class PickupCreate(PickupBase):
    pass

class Pickup(PickupBase):
    id: int

    class Config:
        orm_mode = True

# ProductReceipt schemas
class ProductReceiptBase(BaseModel):
    ProductID: int
    ReceiptID: int
    RescaledWeight: float

class ProductReceiptCreate(ProductReceiptBase):
    pass

class ProductReceiptUpdate(BaseModel):
    ProductID: Optional[int] = None
    ReceiptID: Optional[int] = None
    RescaledWeight: Optional[int] = None

class ProductReceipt(ProductReceiptBase):
    ProductReceiptID: int

    class Config:
        from_attributes = True

class HarborGuardBase(BaseModel):
    HarbourName: str
    Location: str
    phone: str = None
    OpeningHour: time
    ClosingHour: time

    class Config:
        orm_mode = True

class HarborGuardCreate(HarborGuardBase):
    pass

class HarborGuardUpdate(HarborGuardBase):
    pass

class HarborGuardInDB(HarborGuardBase):
    HarbourID: int

    class Config:
        orm_mode = True

#warehouse stock

class WarehouseStockHistoryBase(BaseModel):
    old_stock: int
    new_stock: int
    change_amount: str  # Changed to str to include the formatted change amount
    change_date: datetime

    class Config:
        orm_mode = True
        from_attributes = True

# WAREHOUSE LOCATION
class WarehouseBase(BaseModel):
    email: EmailStr
    phone: Optional[str] = None
    TotalStock: int
    Capacity: int
    location: Optional[str] = None
    created_at: date

class WarehouseCreate(WarehouseBase):
    pass

class WarehouseUpdate(BaseModel):
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    TotalStock: Optional[int] = None
    Capacity: Optional[int] = None
    location: Optional[str] = None

class Warehouse(WarehouseBase):
    id: int  # Assuming an 'id' field is automatically generated by the database
    stock_history: List[WarehouseStockHistoryBase] = []

    class Config:
        orm_mode = True
        from_attributes = True # This setting is crucial for compatibility with ORMs like SQLAlchemy

#xyzuser

class XYZuserBase(BaseModel):
    WarehouseID: int
    userID: int

class XYZuserCreate(XYZuserBase):
    pass

class XYZuserUpdate(XYZuserBase):
    pass

class XYZuser(XYZuserBase):
    id: int

    class Config:
        orm_mode = True

class WetLeaves(BaseModel):
    totalWeight: float
    proportions: List[float]

class DriedLeaves(BaseModel):
    totalWeight: float
    proportions: List[float]

class FlouredLeaves(BaseModel):
    totalWeight: float
    proportions: List[float]

class LeavesStatus(BaseModel):
    wetLeaves: WetLeaves
    driedLeaves: DriedLeaves
    flouredLeaves: FlouredLeaves

class ConversionRateResponse(BaseModel):
    id: int
    conversionRate: float
    wetToDry: float
    dryToFloured: float