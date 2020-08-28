from flask import Blueprint, jsonify, request
import pymongo
bp = Blueprint("run_model", __name__)
import constants as const
import userTrees as algo


#-------------USER HANDLER ROUTES-------------------


@bp.route("/add_user",methods=["POST"])
def handle_add_members():
    jn=request.json      # ref_username, username, name, dob
    userData = const.mydb['userData']
    dicts = const.mydb['dicts']
    dicts_response=dicts.find_one({})
    search_response=userData.find_one({'username':jn['ref_username']})
    if (search_response and dicts_response):
        walletData=dicts_response["walletData"]
        treeData=dicts_response["treeData"]
        trees,wallet=algo.startTree(jn['ref_username'],jn['username'],walletData,treeData)

        myquery = dicts.find_one({})
        newvalues = { "$set": { "walletData": wallet, "treeData":trees } }
        dicts_response=dicts.update_one(myquery, newvalues)

        status_response = userData.insert_one(jn)
        if (status_response and dicts_response):
            status_response="Success"
        else:
            status_response="Failure"
    else:
        status_response="Failure"
 
    response = jsonify({"status": status_response,"data":"No data"})
    return response




