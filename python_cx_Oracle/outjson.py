#!user/bin/python
# -*- coding: utf8 -*-
import cx_Oracle
import json


def OracleToJson():
    try:
		db = cx_Oracle.connect('t_fspf_trans_n/t_fspf_trans_n@merge_mcht')
		
        # 创建数据库游标对象 cursor
        # cursor对象支持的方法有execute(sql语句),fetchone(),fetchmany(size),fetchall(),rowcount,close()
		cur = db.cursor()
		sql = """SELECT T.ID AS id,T.TX_DATE AS tx_date,T.TX_TIME AS tx_time,T.STAT AS stat,T.TRACE_NO AS trace,T.IBOX_NO AS ibox_no,T.ORDER_NO AS order_no,T.CUPS_NO AS cups_no,T.AC_NO AS ac_no,T.USER_ID AS user_id,
		T.DISC_CYCLE AS disc_cysle,T.AC_TYPE AS ac_type,T.AC_BANK_NO AS ac_bank,T.TX_AMT AS tx_amt,T.FEE_AMT AS fee_amt,T.TX_CODE AS tx_code,T.TX_NAME AS tx_name,T.TX_SUB_CODE AS tx_sub_code,T.BRNO AS brno,T.LONGITUDE AS longitude,
		T.LATITUDE AS latitude,T.FILL AS fill,T.IBOX11 AS ibox11,T.FD37 AS fd37,T.IBOX41 AS ibox41,T.FD41 AS fd41,T.IBOX42 AS ibox42,T.FD42 AS fd42,T.IBOX43 AS ibox43,T.FD43 AS fd43,T.FDX AS fdx,T.FDXX AS fdxx,T.FDXXX AS fdxxx,T.EXPAND AS expand,T.SETTLEMODE AS settlemode,T.PROMTSID AS promtsid,T.PROMTSMODE AS promtsmode,T.PROMTSVALUE AS promtsvalue,T.PROMTS_RATIO_FEE AS promts_ratio_fee,T.PROMTS_FIXED_FEE AS promts_fixed_fee,T.SERVETYPE AS servetype FROM TBL_N_TXN T WHERE T.TX_DATE='20170304' and cups_no='alpy'"""
		cur.execute(sql)
		data = cur.fetchall()
		#print u'数据库读取的数据', data
		cur.close()
		db.close()
		jsonData = []
		for row in data:
			result = {}
			result['id'] = str(row[0])
			result['tx_date'] = str(row[1])
			result['tx_time'] = str(row[2])
			result['stat'] = str(row[3])
			result['trace_no'] = str(row[4])
			result['ibox_no'] = str(row[5])
			result['order_no'] = str(row[6])
			result['cups_no'] = str(row[7])
			result['ac_no'] = str(row[8])
			result['user_id'] = row[9]
			result['disc_cycle'] = row[10]
			result['ac_type'] = row[11]
			result['ac_bank_no'] = str(row[12])
			result['tx_amt'] = row[13]
			result['fee_amt'] = row[14]
			result['tx_code'] = str(row[15])
			result['tx_name'] = str(row[16])
			result['tx_sub_code'] = str(row[17])
			result['brno'] = str(row[18])
			result['longitude'] = str(row[19])
			result['latitude'] = str(row[20])
			result['fill'] = str(row[21])
			result['ibox11'] = str(row[22])
			result['fd37'] = str(row[23])
			result['ibox41'] = str(row[24])
			result['fd41'] = str(row[25])
			result['ibox42'] = str(row[26])
			result['fd42'] = str(row[27])
			result['ibox43'] = str(row[28])
			result['fd43'] = str(row[29])
			result['fdx'] = row[30]
			result['fdxx'] = str(row[31])
			result['fdxxx'] = str(row[32])
			result['expand'] = row[33]
			result['settlemode'] = str(row[34])
			result['promtsid'] = row[35]
			result['promtsmode'] = str(row[36])
			result['promtsvalue'] = row[37]
			result['promts_ratio_fee'] = row[38]
			result['promts_fixed_fee'] = row[39]
			result['servetype'] = str(row[40])
			#jsonData.append(result)
			#print u'result:', result
			#result['mcht_phone'] ='18588618859'
#			jsonData.append(result)
			jsonStr = json.dumps(result, ensure_ascii=False)  
			f = open(r'D:\getuidata.txt', 'a+')
			# 写数据
			f.write(jsonStr)
			f.write('\n')
			# 关闭文件
			f.close()
    except:
		print 'Oracle connect fail...'
    else:
		jsondatar = json.dumps(jsonData, ensure_ascii=False)
		return jsondatar[1:len(jsondatar) - 1]



if __name__ == '__main__':
	jsonData = OracleToJson()
	#print u'转换为json格式的数据：', json.dumps(jsonData, ensure_ascii=False) 
	print jsonData
#	f = open(r'D:\getuidata.txt', 'w+')
#	# 写数据
#	f.write(jsonData)
#	# 关闭文件
#	f.close()


