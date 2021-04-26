import sys
import pymysql
import traceback
import uuid
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTreeWidgetItem, QMessageBox
from PyQt5.QtGui import QIcon
from MainWindow import Ui_MainWindow
from SetDatabase import Ui_SetDatabase
from SetIdentity import Ui_SetIdentity
from SetSite import Ui_SetSite
from SetRecord import Ui_SetRecord


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.dbParameter = ["127.0.0.1", "root", "", "passwords", 3306]
        # 数据库
        self.actionConnectDatabase.triggered.connect(
            self.commandConnectDatabase)
        self.actionUpdateDatabase.triggered.connect(self.commandUpdateDatabase)
        self.actionCloseDatabase.triggered.connect(self.commandCloseDatabase)
        # 身份
        self.actionNewIdentity.triggered.connect(self.commandNewIdentity)
        self.actionEditIdentity.triggered.connect(self.commandEditIdentity)
        self.actionDeleteIdentity.triggered.connect(self.commandDeleteIdentity)
        # 站点
        self.actionNewSite.triggered.connect(self.commandNewSite)
        self.actionEditSite.triggered.connect(self.commandEditSite)
        self.actionDeleteSite.triggered.connect(self.commandDeleteSite)
        # 记录
        self.actionNewRecord.triggered.connect(self.commandNewRecord)
        self.actionEditRecord.triggered.connect(self.commandEditRecord)
        self.actionDeleteRecord.triggered.connect(self.commandDeleteRecord)
        self.actionCopyUsername.triggered.connect(self.commandCopyUsername)
        self.actionCopyPassword.triggered.connect(self.commandCopyPassword)
        # 初始化
        self.treeRecord.hideColumn(2)
        self.treeRecord.hideColumn(4)
        self.treeRecord.setColumnWidth(0, 300)
        self.treeRecord.setColumnWidth(1, 300)
        self.treeRecord.setItemsExpandable(False)
        self.treeRecord.itemDoubleClicked.connect(self.commandEditRecord)
        self.treeIdentity.setColumnWidth(0, 300)
        self.treeIdentity.setItemsExpandable(False)
        self.treeIdentity.itemDoubleClicked.connect(self.commandEditIdentity)
        self.treeSite.setColumnWidth(0, 300)
        self.treeSite.setColumnWidth(1, 300)
        self.treeSite.setItemsExpandable(False)
        self.treeSite.itemDoubleClicked.connect(self.commandEditSite)
        if not self.commandConnectDatabase():
            exit(0)
        self.commandUpdateDatabase()

    def commandRunSql(self, sql) -> bool:
        try:
            self.dbCursor.execute(sql)
            self.dbDatabase.commit()
        except Exception as exception:
            self.dbDatabase.rollback()
            self.statusbar.showMessage("错误：" + str(exception))
            return False
        else:
            #self.statusbar.showMessage("成功：" + sql)
            return True

    def commandNewDatabase(self):
        self.commandRunSql("""create table passwd(
                                  uuid varchar(32) primary key,
                                  passwd varchar(40) not null,
                                  comment varchar(100)
                              );""")
        self.commandRunSql("""create table sites (
                                  url varchar(40) primary key,
                                  title varchar(40),
                                  comment varchar(100)
                              );""")
        self.commandRunSql("""create table identities (
                                  id varchar(40) primary key,
                                  comment varchar(100)
                              );""")
        self.commandRunSql("""create table records (
                                  url varchar(40),
                                  id varchar(40),
                                  uuid varchar(32),
                                  primary key(url, id),
                                  constraint fk_sites foreign key(url) references sites(url),
                                  constraint fk_identities foreign key(id) references identities(id),
                                  constraint fk_passwd foreign key(uuid) references passwd(uuid)
                              );""")

    def commandConnectDatabase(self) -> bool:
        dialog = MyConnectDatabase(self.dbParameter, self)
        if dialog.exec_():
            try:
                self.dbDatabase.close()
            except:
                pass
            finally:
                self.dbDatabase = pymysql.connect(
                    self.dbParameter[0], self.dbParameter[1], self.dbParameter[2], self.dbParameter[3], self.dbParameter[4])
                self.dbCursor = self.dbDatabase.cursor()
                self.statusbar.showMessage("数据库连接成功")
                return True
        else:
            return False
        # self.commandNewDatabase()

    def commandUpdateDatabase(self):
        # Identity
        if self.commandRunSql("SELECT * FROM identities;"):
            self.dataIdentity = self.dbCursor.fetchall()
            self.treeIdentity.takeTopLevelItem(0)
            root = QTreeWidgetItem(self.treeIdentity)
            root.setText(0, "（无）")
            for row in self.dataIdentity:
                item = QTreeWidgetItem(root, [row[0], row[1]])
            self.treeIdentity.addTopLevelItem(root)
            self.treeIdentity.expandAll()
        # Site
        if self.commandRunSql("SELECT * FROM sites;"):
            self.dataSite = self.dbCursor.fetchall()
            self.treeSite.takeTopLevelItem(0)
            root = QTreeWidgetItem(self.treeSite)
            root.setText(0, "（无）")
            for row in self.dataSite:
                QTreeWidgetItem(root, [row[0], row[1], row[2]])
            self.treeSite.addTopLevelItem(root)
            self.treeSite.expandAll()
        # Record
        if self.commandRunSql("SELECT r.id, r.url, p.passwd, p.comment, p.uuid FROM records r, passwd p where p.uuid = r.uuid;"):
            self.dataRecord = self.dbCursor.fetchall()
            self.treeRecord.takeTopLevelItem(0)
            root = QTreeWidgetItem(self.treeRecord)
            root.setText(0, "（无）")
            for row in self.dataRecord:
                QTreeWidgetItem(root, [row[0], row[1], row[2], row[3], row[4]])
            self.treeRecord.addTopLevelItem(root)
            self.treeRecord.expandAll()

    def commandCloseDatabase(self):
        try:
            self.dbDatabase.close()
        except:
            pass
        finally:
            self.close()

    def commandNewIdentity(self):
        lists = ["prisident@swu.edu.cn", "test"]
        dialog = MyNewIdentity(lists, self)
        if dialog.exec_():
            self.commandRunSql(
                "INSERT INTO identities(id, comment) value('{0}', '{1}');".format(lists[0], lists[1]))
            self.commandUpdateDatabase()

    def commandEditIdentity(self):
        item = self.treeIdentity.currentItem()
        if item and item.text(0) != "（无）":
            lists = [item.text(0), item.text(1)]
            dialog = MyEditIdentity(lists, self)
            if dialog.exec_():
                self.commandRunSql("""UPDATE identities
                                      SET id = '{0}', comment = '{1}'
                                      WHERE id = '{2}'
                                          AND NOT EXISTS (
                                              SELECT *
                                              FROM records
                                              WHERE id = '{2}'
                                          );""".format(lists[0], lists[1], item.text(0)))
                self.commandUpdateDatabase()

    def commandDeleteIdentity(self):
        item = self.treeIdentity.currentItem()
        if item and item.text(0) != "（无）":
            if QMessageBox.information(
                    self, '删除', '是否删除该身份？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
                self.commandRunSql(
                    'DELETE FROM identities WHERE id = "' + item.text(0) + '" AND NOT EXISTS (SELECT * FROM records WHERE id = "' + item.text(0) + '");')
                self.commandUpdateDatabase()

    def commandNewSite(self):
        lists = ["http://swu.edu.cn", "西南大学", "认证系统"]
        dialog = MyNewSite(lists, self)
        if dialog.exec_():
            self.commandRunSql(
                "INSERT INTO sites(url, title, comment) value('{0}', '{1}', '{2}');".format(lists[0], lists[1], lists[2]))
            self.commandUpdateDatabase()

    def commandEditSite(self):
        item = self.treeSite.currentItem()
        if item and item.text(0) != "（无）":
            lists = [item.text(0), item.text(1), item.text(2)]
            dialog = MyEditSite(lists, self)
            if dialog.exec_():
                self.commandRunSql("""UPDATE sites
                                      SET url = '{0}', title = '{1}', comment = '{2}'
                                      WHERE url = '{3}'
                                          AND NOT EXISTS (
                                              SELECT *
                                              FROM records
                                              WHERE url = '{3}'
                                          );""".format(lists[0], lists[1], lists[2], item.text(0)))
                self.commandUpdateDatabase()

    def commandDeleteSite(self):
        item = self.treeSite.currentItem()
        if item and item.text(0) != "（无）":
            if QMessageBox.information(
                    self, '删除', '是否删除该站点？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
                self.dbCursor.execute(
                    'DELETE FROM sites WHERE url = "' + item.text(0) + '" AND NOT EXISTS (SELECT * FROM records WHERE url = "' + item.text(0) + '");')
                self.dbDatabase.commit()
                self.commandUpdateDatabase()

    def commandNewRecord(self):
        lists = ["", "", "123456", "办事大厅"]
        dialog = MyNewRecord(lists, self.dataSite, self.dataIdentity, self)
        if dialog.exec_():
            uuids = uuid.uuid1()
            self.commandRunSql(
                "INSERT INTO passwd(uuid, passwd, comment) value('{0}', '{1}', '{2}');".format(uuids, lists[2], lists[3]))
            self.commandRunSql(
                "INSERT INTO records(url, id, uuid) value('{0}', '{1}', '{2}');".format(lists[0], lists[1], uuids))
            self.commandUpdateDatabase()

    def commandEditRecord(self):
        item = self.treeRecord.currentItem()
        if item and item.text(0) != "（无）":
            lists = [item.text(0), item.text(1), item.text(
                2), item.text(3), item.text(4)]
            dialog = MyEditRecord(lists, self.dataSite,
                                  self.dataIdentity, self)
            if dialog.exec_():
                self.commandRunSql("UPDATE passwd SET passwd = '{0}', comment = '{1}' WHERE uuid = '{2}';".format(
                    lists[2], lists[3], lists[4]))
                self.commandRunSql("DELETE FROM records WHERE id = '{0}' AND url = '{1}';".format(
                    item.text(0), item.text(1)))
                self.commandRunSql("INSERT INTO records(url, id, uuid) value('{0}', '{1}', '{2}');".format(
                    lists[0], lists[1], lists[4]))
                self.commandUpdateDatabase()

    def commandDeleteRecord(self):
        item = self.treeRecord.currentItem()
        if item and item.text(0) != "（无）":
            if QMessageBox.information(
                    self, '删除', '是否删除该记录？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
                self.dbCursor.execute(
                    "DELETE FROM records WHERE id = '{0}' AND url = '{1}';".format(item.text(0), item.text(1)))
                self.dbCursor.execute(
                    "DELETE FROM passwd WHERE uuid = '{0}';".format(item.text(4)))
                self.dbDatabase.commit()
                self.commandUpdateDatabase()

    def commandCopyUsername(self):
        item = self.treeRecord.currentItem()
        if item and item.text(0) != "（无）":
            clipboard = QApplication.clipboard()
            clipboard.setText(item.text(0))

    def commandCopyPassword(self):
        item = self.treeRecord.currentItem()
        if item and item.text(0) != "（无）":
            clipboard = QApplication.clipboard()
            clipboard.setText(item.text(2))

    def closeEvent(self, event):
        try:
            self.dbDatabase.close()
        except:
            pass
        finally:
            event.accept()


class MyConnectDatabase(QDialog, Ui_SetDatabase):
    def __init__(self, dbParameter, parent=None):
        super(MyConnectDatabase, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("连接数据库")
        self.dbParameter = dbParameter
        self.lineEditHost.setText(self.dbParameter[0])
        self.lineEditUser.setText(self.dbParameter[1])
        self.lineEditPassword.setText(self.dbParameter[2])
        self.lineEditDatabase.setText(self.dbParameter[3])
        self.lineEditPort.setText(str(self.dbParameter[4]))
        self.pushButtonTestConnection.clicked.connect(
            self.commandTestConnection)
        self.buttonBox.accepted.connect(self.commandAccept)

    def commandSetParameter(self):
        self.dbParameter[0] = self.lineEditHost.text()
        self.dbParameter[1] = self.lineEditUser.text()
        self.dbParameter[2] = self.lineEditPassword.text()
        self.dbParameter[3] = self.lineEditDatabase.text()
        self.dbParameter[4] = int(self.lineEditPort.text())

    def commandTestConnection(self) -> bool:
        try:
            self.commandSetParameter()
            db = pymysql.connect(
                self.dbParameter[0], self.dbParameter[1], self.dbParameter[2], self.dbParameter[3], self.dbParameter[4])
            db.close()
        except Exception as exception:
            self.plainTextEditTestResult.setPlainText(
                "错误\n" + str(exception))
            return False
        else:
            self.plainTextEditTestResult.setPlainText("成功")
            return True

    def commandAccept(self):
        if self.commandTestConnection():
            self.accept()


class MyNewIdentity(QDialog, Ui_SetIdentity):
    def __init__(self, lists, parent=None):
        super(MyNewIdentity, self).__init__(parent)
        self.setupUi(self)
        self.lists = lists
        self.lineEditAccount.setText(lists[0])
        self.plainTextComment.setPlainText(lists[1])
        self.setWindowTitle("添加身份")
        self.buttonBox.accepted.connect(self.commandAccept)

    def commandAccept(self):
        self.lists[0] = self.lineEditAccount.text()
        self.lists[1] = self.plainTextComment.toPlainText()
        self.accept()


class MyEditIdentity(QDialog, Ui_SetIdentity):
    def __init__(self, lists, parent=None):
        super(MyEditIdentity, self).__init__(parent)
        self.setupUi(self)
        self.lists = lists
        self.lineEditAccount.setText(lists[0])
        self.plainTextComment.setPlainText(lists[1])
        self.setWindowTitle("编辑身份")
        self.buttonBox.accepted.connect(self.commandAccept)

    def commandAccept(self):
        self.lists[0] = self.lineEditAccount.text()
        self.lists[1] = self.plainTextComment.toPlainText()
        self.accept()


class MyNewSite(QDialog, Ui_SetSite):
    def __init__(self, lists, parent=None):
        super(MyNewSite, self).__init__(parent)
        self.setupUi(self)
        self.lists = lists
        self.lineEditAddress.setText(lists[0])
        self.lineEditTitle.setText(lists[1])
        self.plainTextComment.setPlainText(lists[2])
        self.setWindowTitle("添加站点")
        self.buttonBox.accepted.connect(self.commandAccept)

    def commandAccept(self):
        self.lists[0] = self.lineEditAddress.text()
        self.lists[1] = self.lineEditTitle.text()
        self.lists[2] = self.plainTextComment.toPlainText()
        self.accept()


class MyEditSite(QDialog, Ui_SetSite):
    def __init__(self, lists, parent=None):
        super(MyEditSite, self).__init__(parent)
        self.setupUi(self)
        self.lists = lists
        self.lineEditAddress.setText(lists[0])
        self.lineEditTitle.setText(lists[1])
        self.plainTextComment.setPlainText(lists[2])
        self.setWindowTitle("编辑站点")
        self.buttonBox.accepted.connect(self.commandAccept)

    def commandAccept(self):
        self.lists[0] = self.lineEditAddress.text()
        self.lists[1] = self.lineEditTitle.text()
        self.lists[2] = self.plainTextComment.toPlainText()
        self.accept()


class MyNewRecord(QDialog, Ui_SetRecord):
    def __init__(self, lists, tupleSite, tupleIdentity, parent=None):
        super(MyNewRecord, self).__init__(parent)
        self.setupUi(self)
        self.lists = lists
        for row in tupleSite:
            self.comboBoxSite.addItem(row[0])
        for row in tupleIdentity:
            self.comboBoxIdentity.addItem(row[0])
        self.lineEditPassword.setText(lists[2])
        self.plainTextComment.setPlainText(lists[3])
        self.setWindowTitle("添加记录")
        self.buttonBox.accepted.connect(self.commandAccept)

    def commandAccept(self):
        self.lists[0] = self.comboBoxSite.currentText()
        self.lists[1] = self.comboBoxIdentity.currentText()
        self.lists[2] = self.lineEditPassword.text()
        self.lists[3] = self.plainTextComment.toPlainText()
        self.accept()


class MyEditRecord(QDialog, Ui_SetRecord):
    def __init__(self, lists, tupleSite, tupleIdentity, parent=None):
        super(MyEditRecord, self).__init__(parent)
        self.setupUi(self)
        self.lists = lists
        for row in tupleSite:
            self.comboBoxSite.addItem(row[0])
        for row in tupleIdentity:
            self.comboBoxIdentity.addItem(row[0])
        self.comboBoxSite.setCurrentText(lists[0])
        self.comboBoxIdentity.setCurrentText(lists[1])
        self.lineEditPassword.setText(lists[2])
        self.plainTextComment.setPlainText(lists[3])
        self.setWindowTitle("编辑记录")
        self.buttonBox.accepted.connect(self.commandAccept)

    def commandAccept(self):
        self.lists[0] = self.comboBoxSite.currentText()
        self.lists[1] = self.comboBoxIdentity.currentText()
        self.lists[2] = self.lineEditPassword.text()
        self.lists[3] = self.plainTextComment.toPlainText()
        self.accept()


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = MyMainWindow()
    ex.show()
    sys.exit(app.exec_())
