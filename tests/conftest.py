from pathlib import Path

import pandas as pd
import numpy as np
import pytest

import lidar
import rospy


@pytest.fixture()
def testbag1():
    return Path(__file__).parent.absolute() / "testdata/test.bag"


@pytest.fixture()
def testset(testbag1):
    return lidar.Dataset(testbag1, lidar_name="ouster", keep_zeros=False)


@pytest.fixture()
def testset_withzero(testbag1):
    return lidar.Dataset(testbag1, lidar_name="ouster", keep_zeros=True)


@pytest.fixture()
def testframe(testset):
    return testset[1]


@pytest.fixture()
def testframe_withzero(testset_withzero):
    return testset_withzero[1]


@pytest.fixture()
def testframe_mini_df():
    columns = [
        "x",
        "y",
        "z",
        "intensity",
        "t",
        "reflectivity",
        "ring",
        "noise",
        "range",
    ]
    np.random.seed(5)
    df1 = pd.DataFrame(np.zeros(shape=(1, len(columns))), columns=columns)
    df2 = pd.DataFrame(np.ones(shape=(1, len(columns))), columns=columns)
    df3 = pd.DataFrame(
        np.random.randint(0, 1000, size=(5, len(columns))) * np.random.random(),
        columns=columns,
    )
    return pd.concat([df1, df2, df3]).reset_index(drop=True)


@pytest.fixture()
def reference_data_with_zero_dataframe():
    filename = (
        Path(__file__).parent.absolute() / "testdata/testframe_withzero_dataframe.pkl"
    )
    return pd.read_pickle(filename)


@pytest.fixture()
def reference_pointcloud_withzero_dataframe():
    filename = (
        Path(__file__).parent.absolute() / "testdata/testframe_withzero_pointcloud.pkl"
    )
    return pd.read_pickle(filename)


@pytest.fixture()
def testframe_mini(testframe_mini_df):
    return lidar.Frame(testframe_mini_df, rospy.rostime.Time(50))