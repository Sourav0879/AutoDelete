#=========================================================================
# [AutoDelete - Telegram bot to delete messages after specific time]      
# Copyright (C) 2022 Arunkumar Shibu                       
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#=========================================================================

import os

API_ID       = int(os.environ.get("API_ID", "26083023"))
API_HASH     = os.environ.get("API_HASH", "4dd1e00d9d977f74435a83927273feba")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "7022937720:AAGmoo7EYLqnOc7oDQlvF-xMCO6Mchq2NNg")
SESSION      = os.environ.get("SESSION", "BQFB9jMARMpSHGH6U3u-bWlx2K3CvNHs4rc_j0O2Mz5WrXAOH_ilBAqY8rlPTDMH-k9dHx4ipKcKRmhSVBpM2z5ZVp7cim2KiYkeC02FFg_mVgvLpSYSPmRlNNujS3lOZ3KsHHoA6PVpyfeKXIpY9PXNrXQzBEiLILMZeqTF2eSJmTCK6dwuvhVF06TyH88lRi7jKvnWwSXS70Fx42vEhaaDy2u7uHuD59G6IJsz2ZPfq9K8vURVbuhhDi84PJIUXkY5M_UGEVYTNJYlE36M1yXNN_GCICF-86459VKUkFMiTJIF7W5WGXIb99EBFRxscZSHx2smjDp2mmqgvtRU3N_iFWTuyAAAAAHEqf9yAA")
TIME         = int(os.environ.get("TIME", 10800))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1002027376994").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://souravbosu0207:rHaqpU42HDK93WwW@cluster0.za4h6oa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
PORT         = os.environ.get("PORT", "8080")
