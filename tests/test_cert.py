from os import listdir
from os.path import join
import unittest

from ninjadroid.errors.cert_parsing_error import CertParsingError
from ninjadroid.errors.parsing_error import ParsingError
from ninjadroid.parsers.cert import Cert


# TODO: refactor these tests...
class TestCert(unittest.TestCase):
    """
    UnitTest for cert.py.

    RUN: python -m unittest -v tests.test_cert
    """

    cert_properties = {
        "CERT.RSA": {
            "name": "CERT.RSA",
            "size": 906,
            "md5": "5026e73a2f0d8091aaf7908cffbc425e",
            "sha1": "37210614d362672e19cdd7940b7f5037de6cbcb8",
            "sha256": "0ba1a5ba50b277bb37d05e8b9d2c6422aad49b90c08e7136d2d7c204ceaaf412",
            "sha512": "e16ce3b471f10043be642472dc4f0156dccb434331c0c1ca19470b7dc0d025d4bb512fc5e77e78011e704b69fe0872e6fd7dee648e87401062f59149695f36f5",
            "serial_number": "558e7595",
            "validity": {
                "from": "2015-06-27 10:06:13Z",
                "until": "2515-02-26 10:06:13Z",
            },
            "fingerprint_sha1": "5A:C0:6C:32:63:7F:5D:BE:CA:F9:38:38:4C:FA:FF:ED:20:52:43:B6",
            "fingerprint_sha256": "E5:15:CC:BC:5E:BF:B2:9D:A6:13:03:63:CF:19:33:FA:CE:AF:DC:ED:5D:2F:F5:98:7C:CE:37:13:64:4A:CF:77",
            "fingerprint_signature": "SHA1withRSA",
            "fingerprint_version": "3",
            "owner": {
                "name": "Name",
                "email": "",
                "unit": "Unit",
                "organization": "Organization",
                "city": "City",
                "state": "State",
                "country": "XX",
                "domain": "",
            },
            "issuer": {
                "name": "Name",
                "email": "",
                "unit": "Unit",
                "organization": "Organization",
                "city": "City",
                "state": "State",
                "country": "XX",
                "domain": "",
            },
        },
    }

    @classmethod
    def setUpClass(cls):
        cls.certs = {}

        for filename in listdir(join("tests", "data")):
            if filename in cls.cert_properties:
                cls.certs[filename] = Cert(join("tests", "data", filename), filename)
                # print(cls.certs[filename].dump())

    def test_init(self):
        for filename in self.certs:
            cert = self.certs[filename]

            self.assertTrue(cert is not None)
            self.assertTrue(type(cert) is Cert)

    def test_init_with_non_existing_file(self):
        with self.assertRaises(ParsingError):
            Cert(join("tests", "data", "aaa_this_is_a_non_existent_file_xxx"))

    def test_init_with_non_cert_file(self):
        with self.assertRaises(CertParsingError):
            Cert(join("tests", "data", "Example.apk"))
            Cert(join("tests", "data", "AndroidManifest.xml"))
            Cert(join("tests", "data", "classes.dex"))

    def test_get_raw_file(self):
        for filename in self.certs:
            raw_file = self.certs[filename].get_raw_file()

            self.assertTrue(len(raw_file) > 0)

    def test_get_file_name(self):
        for filename in self.certs:
            name = self.certs[filename].get_file_name()

            self.assertEqual(self.cert_properties[filename]["name"], name)

    def test_get_size(self):
        for filename in self.certs:
            size = self.certs[filename].get_size()

            self.assertEqual(self.cert_properties[filename]["size"], size)

    def test_get_md5(self):
        for filename in self.certs:
            md5 = self.certs[filename].get_md5()

            self.assertEqual(self.cert_properties[filename]["md5"], md5)

    def test_get_sha1(self):
        for filename in self.certs:
            sha1 = self.certs[filename].get_sha1()

            self.assertEqual(self.cert_properties[filename]["sha1"], sha1)

    def test_get_sha256(self):
        for filename in self.certs:
            sha256 = self.certs[filename].get_sha256()

            self.assertEqual(self.cert_properties[filename]["sha256"], sha256)

    def test_get_sha512(self):
        for filename in self.certs:
            sha512 = self.certs[filename].get_sha512()

            self.assertEqual(self.cert_properties[filename]["sha512"], sha512)

    def test_get_serial_number(self):
        for filename in self.certs:
            serial_number = self.certs[filename].get_serial_number()

            self.assertEqual(self.cert_properties[filename]["serial_number"], serial_number)

    def test_get_validity(self):
        for filename in self.certs:
            validity = self.certs[filename].get_validity()

            self.assertEqual(self.cert_properties[filename]["validity"], validity)

    def test_get_fingerprint_sha1(self):
        for filename in self.certs:
            sha1 = self.certs[filename].get_fingerprint_sha1()

            self.assertEqual(self.cert_properties[filename]["fingerprint_sha1"], sha1)

    def test_get_fingerprint_sha256(self):
        for filename in self.certs:
            sha256 = self.certs[filename].get_fingerprint_sha256()

            self.assertEqual(self.cert_properties[filename]["fingerprint_sha256"], sha256)

    def test_get_fingerprint_signature(self):
        for filename in self.certs:
            signature = self.certs[filename].get_fingerprint_signature()

            self.assertTrue(signature.startswith(self.cert_properties[filename]["fingerprint_signature"]))

    def test_get_fingerprint_version(self):
        for filename in self.certs:
            version = self.certs[filename].get_fingerprint_version()

            self.assertEqual(self.cert_properties[filename]["fingerprint_version"], version)

    def test_get_owner(self):
        for filename in self.certs:
            owner = self.certs[filename].get_owner()

            self.assertEqual(self.cert_properties[filename]["owner"]["name"], owner["name"])
            self.assertEqual(self.cert_properties[filename]["owner"]["email"], owner["email"])
            self.assertEqual(self.cert_properties[filename]["owner"]["unit"], owner["unit"])
            self.assertEqual(self.cert_properties[filename]["owner"]["organization"], owner["organization"])
            self.assertEqual(self.cert_properties[filename]["owner"]["city"], owner["city"])
            self.assertEqual(self.cert_properties[filename]["owner"]["state"], owner["state"])
            self.assertEqual(self.cert_properties[filename]["owner"]["country"], owner["country"])
            self.assertEqual(self.cert_properties[filename]["owner"]["domain"], owner["domain"])

    def test_get_issuer(self):
        for filename in self.certs:
            issuer = self.certs[filename].get_issuer()

            self.assertEqual(self.cert_properties[filename]["issuer"]["name"], issuer["name"])
            self.assertEqual(self.cert_properties[filename]["issuer"]["email"], issuer["email"])
            self.assertEqual(self.cert_properties[filename]["issuer"]["unit"], issuer["unit"])
            self.assertEqual(self.cert_properties[filename]["issuer"]["organization"], issuer["organization"])
            self.assertEqual(self.cert_properties[filename]["issuer"]["city"], issuer["city"])
            self.assertEqual(self.cert_properties[filename]["issuer"]["state"], issuer["state"])
            self.assertEqual(self.cert_properties[filename]["issuer"]["country"], issuer["country"])
            self.assertEqual(self.cert_properties[filename]["issuer"]["domain"], issuer["domain"])

    def test_dump(self):
        for filename in self.certs:
            dump = self.certs[filename].dump()

            self.assertEqual(self.cert_properties[filename]["name"], dump["file"])
            self.assertEqual(self.cert_properties[filename]["size"], dump["size"])
            self.assertEqual(self.cert_properties[filename]["md5"], dump["md5"])
            self.assertEqual(self.cert_properties[filename]["sha1"], dump["sha1"])
            self.assertEqual(self.cert_properties[filename]["sha256"], dump["sha256"])
            self.assertEqual(self.cert_properties[filename]["sha512"], dump["sha512"])
            self.assertEqual(self.cert_properties[filename]["serial_number"], dump["serial_number"])


if __name__ == "__main__":
    unittest.main()
